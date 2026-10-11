# Shaders and Compositing

Geometry Script can also build shader and compositor node trees. Each tree type has its own module, because each accepts a different set of nodes:

| Module | Decorators | Builds |
|---|---|---|
| `geometry_script` | `@tree` (or `@geometry`) | Geometry Nodes groups |
| `geometry_script.shader` | `@shader`, `@material`, `@world` | Shader node groups, materials and worlds |
| `geometry_script.compositor` | `@compositor` | Compositor node groups |

Each module has every node its tree type accepts as a typed function, plus the same types (`Color`, `Vector`, `Shader`, ...) and `Socket` arithmetic as the main module. Some names exist in several modules with different nodes behind them. For example, `normal()` is the *Normal* input in Geometry Nodes, but the *Normal* vector node in shaders. Import each module where it's used. If a node is used in the wrong kind of tree, the error says which module it belongs to.

```python
from geometry_script.shader import *   # A shader-only script
```

```python
from geometry_script import *          # Geometry nodes
from geometry_script import shader as sh

sh.principled_bsdf(...)                # Shader nodes, behind a namespace
```

## Materials

`@material` builds a material from a function with no parameters. Return the surface shader:

```python
from geometry_script.shader import *

@material("Gold")
def gold():
    return principled_bsdf(
        base_color=(1.0, 0.77, 0.34, 1.0),
        metallic=1.0,
        roughness=0.2,
    ).bsdf
```

To use the other inputs of the *Material Output*, return a dictionary:

```python
@material("Rough Stone")
def rough_stone():
    height = noise_texture(scale=8.0).factor
    return {
        "surface": principled_bsdf(base_color=(0.4, 0.4, 0.38, 1.0)).bsdf,
        "displacement": displacement(height=height, scale=0.05).displacement,
    }
```

The material is rebuilt in place each time the script runs, so objects that use it keep it. Calling the decorated function returns the material, so a geometry tree can assign it:

```python
@tree("Golden Cube")
def golden_cube():
    return set_material(geometry=cube().mesh, material=gold()).geometry
```

## Shader Node Groups

`@shader` builds a reusable shader node group. It works like `@tree`: parameters become group inputs, return values become group outputs, and calling it while building a material, world or another shader group adds a group node.

```python
@shader("Stripes")
def stripes(color_a: Color, color_b: Color, scale: float = 6.0):
    wave = wave_texture(scale=scale)
    return mix(data_type="RGBA", factor=wave.factor, a=color_a, b=color_b).result

@material("Striped")
def striped():
    color = stripes((0.9, 0.3, 0.1, 1.0), (0.1, 0.1, 0.1, 1.0), scale=10.0)
    return principled_bsdf(base_color=color).bsdf
```

Materials and worlds have no inputs of their own, so put anything you'd like to adjust in Blender's UI into a `@shader` group.

`@repeat_zone` and `@closure_zone` work in shader trees too.

## Worlds

`@world` builds a world the same way. Pass `scene=True` to make it the active scene's world:

```python
@world("Studio", scene=True)
def studio():
    return background(color=(0.05, 0.06, 0.08, 1.0), strength=1.0).background
```

## Compositing

`@compositor` builds a compositor node group from `geometry_script.compositor`. Pass `scene=True` to use it as the active scene's compositor. Its first output is the final image:

```python
from geometry_script.compositor import *

@compositor("Soft Glow", scene=True)
def soft_glow(strength: float = 0.3):
    image = render_layers().image
    glow = blur(image=image, size=(20, 20)).image
    return mix(data_type="RGBA", blend_type="SCREEN", factor=strength, a=image, b=glow).result
```

Without `scene=True`, the group can be used as a node in other compositor groups, just like a `@tree` inside another `@tree`.
