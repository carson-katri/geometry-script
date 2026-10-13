"""Compact, token-cheap descriptions of the generated node functions.

Reads the generated node modules with ``ast``, so it runs without Blender:

    python3 tools/describe.py set_position mesh_to_points
    python3 tools/describe.py --search "points on faces"
    python3 tools/describe.py --tree shader principled_bsdf

Inside Blender, ``geometry_script.describe(...)`` and ``geometry_script.search(...)``
print the same text.
"""

from __future__ import annotations

import ast
import re
import sys
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import cache
from pathlib import Path


# The generated module for each tree type, by the name ``tree=`` takes.
NODE_MODULES = {
    "geometry": Path(__file__).with_name("nodes.py"),
    "shader": Path(__file__).with_name("shader_nodes.py"),
    "compositor": Path(__file__).with_name("compositor_nodes.py"),
}
TREES_BY_TYPE = {
    "GeometryNodeTree": "geometry",
    "ShaderNodeTree": "shader",
    "CompositorNodeTree": "compositor",
}
_STRUCTURES = ("Field", "Grid", "List")


@dataclass
class _Parameter:
    name: str
    annotation: str
    default: str | None
    help: str = ""


@dataclass
class _Node:
    function_name: str
    label: str
    description: str
    bl_idname: str
    parameters: list[_Parameter] = field(default_factory=list)
    outputs: list[tuple[str, str]] = field(default_factory=list)
    item_outputs: bool = False
    # Python name by Blender socket identifier, and by socket name as a fallback.
    input_names: dict[str, str] = field(default_factory=dict)
    output_names: dict[str, str] = field(default_factory=dict)


def _split_union(annotation: str) -> list[str]:
    """Split ``a | b[c | d]`` on its top-level ``|``."""
    parts, depth, current = [], 0, ""
    for character in annotation:
        if character in "[(":
            depth += 1
        elif character in "])":
            depth -= 1
        if character == "|" and depth == 0:
            parts.append(current.strip())
            current = ""
        else:
            current += character
    parts.append(current.strip())
    return [part for part in parts if part]


def compact_type(annotation: str) -> str:
    """``float | Field[float] | Socket[...]`` -> ``float field``."""
    if annotation.startswith("Socket[") and annotation.endswith("]"):
        annotation = annotation[len("Socket["):-1]
    literal = re.fullmatch(r"typing\.Literal\[(.*)\]", annotation)
    if literal:
        return "|".join(value.strip().strip("'\"") for value in literal.group(1).split(","))
    bases: dict[str, list[str]] = {}
    for part in _split_union(annotation):
        if part.startswith("Socket[") or part == "None":
            continue
        if part.startswith("typing.Literal["):
            bases.setdefault(compact_type(part), [])
            continue
        structure = next((s for s in _STRUCTURES if part.startswith(f"{s}[")), None)
        if structure:
            base = part[len(structure) + 1:-1]
            bases.setdefault(base, []).append(structure.lower())
        else:
            bases.setdefault(part, [])
    # Group bases that accept the same structures: "float|int field".
    groups: dict[tuple[str, ...], list[str]] = {}
    for base, structures in bases.items():
        groups.setdefault(tuple(structures), []).append(base)
    rendered = []
    for structures, names in groups.items():
        text = "|".join(names)
        if structures:
            text += " " + "/".join(structures)
        rendered.append(text)
    return ", ".join(rendered) if len(rendered) > 1 else (rendered[0] if rendered else "any")


def _compact_default(node: ast.expr | None) -> str | None:
    if node is None:
        return None
    try:
        value = ast.literal_eval(node)
    except ValueError:
        return ast.unparse(node)

    def short(item: object) -> str:
        if isinstance(item, float):
            return f"{item:.6g}" if item == item else "nan"
        return repr(item)

    if isinstance(value, tuple):
        return "(" + ", ".join(short(item) for item in value) + ")"
    return short(value)


def _docstring_parts(docstring: str) -> tuple[str, dict[str, str]]:
    description, _, args = docstring.partition("Args:\n")
    if docstring.startswith("Args:\n"):
        description, args = "", docstring[len("Args:\n"):]
    helps = {}
    for line in args.splitlines():
        name, separator, text = line.strip().partition(":")
        if separator:
            helps[name] = " ".join(text.split())
    return description.strip(), helps


def _check_tree(tree: str) -> None:
    if tree not in NODE_MODULES:
        raise ValueError(f"tree must be one of {list(NODE_MODULES)!r}, not {tree!r}.")


@cache
def _nodes(tree: str = "geometry") -> dict[str, _Node]:
    _check_tree(tree)
    path = NODE_MODULES[tree]
    if not path.is_file():
        raise FileNotFoundError(
            f"{path.name} hasn't been generated. Run "
            "`blender -b --factory-startup --python code_generator/node_functions_generator.py` "
            "from the repository root, or load the add-on in Blender once."
        )
    module = ast.parse(path.read_text(encoding="utf-8"))
    classes = {item.name: item for item in module.body if isinstance(item, ast.ClassDef)}
    nodes = {}
    for item in module.body:
        if not isinstance(item, ast.FunctionDef) or item.name.startswith("_"):
            continue
        docstring = ast.get_docstring(item, clean=False) or ""
        description, helps = _docstring_parts(docstring)
        call = next(
            (n for n in ast.walk(item) if isinstance(n, ast.Call)
             and isinstance(n.func, ast.Name) and n.func.id == "_node_function"),
            None,
        )
        bl_idname = ast.literal_eval(call.args[0]) if call and call.args else ""
        node = _Node(item.name, item.name, description, bl_idname)
        for keyword in call.keywords if call else ():
            if keyword.arg in {"input_sockets", "output_sockets"} and isinstance(keyword.value, ast.Dict):
                names = node.input_names if keyword.arg == "input_sockets" else node.output_names
                for key, reference in zip(keyword.value.keys, keyword.value.values):
                    python_name = ast.literal_eval(key) if key is not None else ""
                    if not python_name or not isinstance(reference, ast.Tuple):
                        continue
                    identifier, socket_name = (ast.literal_eval(r) for r in reference.elts[:2])
                    names.setdefault(socket_name, python_name)
                    names[identifier] = python_name
        arguments = item.args
        for argument, default in zip(arguments.kwonlyargs, arguments.kw_defaults):
            annotation = ast.unparse(argument.annotation) if argument.annotation else "any"
            node.parameters.append(_Parameter(
                argument.arg, annotation, _compact_default(default), helps.get(argument.arg, "")
            ))
        if arguments.kwarg:
            node.parameters.append(_Parameter(
                f"**{arguments.kwarg.arg}", "any", None, helps.get(arguments.kwarg.arg, "")
            ))
        output_class = classes.get(ast.unparse(item.returns) if item.returns else "")
        if output_class is not None:
            node.item_outputs = any(ast.unparse(b) == "ItemOutputs" for b in output_class.bases)
            class_doc = ast.get_docstring(output_class) or ""
            match = re.match(r"Outputs from (.+?): (.*)", class_doc, re.DOTALL)
            if match:
                node.label = match.group(1)
                node.description = node.description or match.group(2).strip()
            for statement in output_class.body:
                if isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name):
                    node.outputs.append(
                        (statement.target.id, ast.unparse(statement.annotation))
                    )
        nodes[item.name] = node
    return nodes


def node_for_bl_idname(bl_idname: str, tree_type: str = "GeometryNodeTree") -> _Node | None:
    """The generated function for a Blender node type in a ``tree_type`` tree, if any."""
    tree = TREES_BY_TYPE.get(tree_type)
    if tree is None:
        return None
    return next((n for n in _nodes(tree).values() if n.bl_idname == bl_idname), None)


def _other_trees(tree: str, has: Callable[[str], bool]) -> str:
    """A hint naming the other tree types for which ``has(tree)`` holds."""
    others = [other for other in NODE_MODULES if other != tree and has(other)]
    if not others:
        return ""
    return " Found for " + ", ".join(f"tree={other!r}" for other in others) + "."


def describe_text(*names: str, tree: str = "geometry") -> str:
    """The compact signature of each named node function of ``tree`` nodes."""
    nodes = _nodes(tree)
    blocks = []
    for name in names:
        node = nodes.get(name)
        if node is None:
            message = f"No {tree} node function {name!r}."
            message += _other_trees(tree, lambda other: name in _nodes(other))
            close = _search(name, tree)
            if close:
                message += " Closest:\n" + search_text(name, limit=5, tree=tree)
            blocks.append(message)
            continue
        lines = [f"{node.function_name}  # {node.label}: {node.description}".rstrip(": ")]
        for parameter in node.parameters:
            line = f"  {parameter.name}: {compact_type(parameter.annotation)}"
            if parameter.default == "None":
                # None leaves a socket unlinked, or lets a type setting be inferred.
                if "typing.Literal[" in parameter.annotation:
                    line += " = inferred"
            elif parameter.default is not None:
                line += f" = {parameter.default}"
            help = parameter.help.replace("Inferred from the linked inputs when None.", "").strip()
            if help:
                line += f"  # {help}"
            lines.append(line)
        outputs = ", ".join(f".{name}: {compact_type(t)}" for name, t in node.outputs)
        if node.item_outputs:
            outputs += (", " if outputs else "") + "plus one output per item, by name"
        lines.append(f"  -> {outputs or 'nothing'}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def _fold(text: str) -> str:
    """Lowercase without accents, so "bezier" finds "Bézier"."""
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(character for character in decomposed if not unicodedata.combining(character))


def _search(query: str, tree: str) -> list[_Node]:
    """``tree`` node functions whose name, label or description match ``query``, best first."""
    words = [word for word in re.split(r"[\s_]+", _fold(query)) if word]
    squashed_query = "".join(words)
    scored = []
    for node in _nodes(tree).values():
        name = _fold(f"{node.function_name} {node.label}")
        description = _fold(node.description)
        score = sum(3 if word in name else 1 if word in description else 0 for word in words)
        if squashed_query in name.replace("_", "").replace(" ", ""):
            score += 5
        if score:
            scored.append((-score, node.function_name, node))
    scored.sort()
    return [node for _, _, node in scored]


def search_text(query: str, limit: int = 12, tree: str = "geometry") -> str:
    """``tree`` node functions whose name, label or description match ``query``, best first."""
    lines = []
    for node in _search(query, tree)[:limit]:
        description = node.description if len(node.description) <= 90 else node.description[:87] + "..."
        lines.append(f"{node.function_name}  # {node.label}: {description}".rstrip(": "))
    if lines:
        return "\n".join(lines)
    hint = _other_trees(tree, lambda other: bool(_search(query, other)))
    return f"No {tree} node functions match {query!r}.{hint}"


def describe(*names: str, tree: str = "geometry") -> None:
    """Print the compact signature of each named node function.

    ``tree`` picks the node set: "geometry", "shader" or "compositor".
    """
    print(describe_text(*names, tree=tree))


def search(query: str, limit: int = 12, tree: str = "geometry") -> None:
    """Print node functions matching ``query``, best first.

    ``tree`` picks the node set: "geometry", "shader" or "compositor".
    """
    print(search_text(query, limit, tree))


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {"-h", "--help"}:
        print((__doc__ or "").strip())
        return 0
    tree = "geometry"
    if argv[0] == "--tree" and len(argv) > 1:
        tree, argv = argv[1], argv[2:]
        if tree not in NODE_MODULES:
            print(f"--tree must be one of {', '.join(NODE_MODULES)}", file=sys.stderr)
            return 2
    try:
        if argv and argv[0] == "--search":
            search(" ".join(argv[1:]), tree=tree)
        else:
            describe(*argv, tree=tree)
    except FileNotFoundError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
