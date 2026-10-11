# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Set the `geometry_script` module to the current module in case the folder is named differently.
import sys
sys.modules['geometry_script'] = sys.modules[__name__]

import bpy
import os
import webbrowser
from pathlib import Path

from .preferences import GeometryScriptPreferences
from .api.tree import tree
from .api.runtime import Socket
from .api.types import *
from .api.zones import (
    ForEachResult,
    closure_zone,
    for_each_element,
    repeat_zone,
    simulation_zone,
)
from .api.nodes import *
from .api.aliases import math
from .api import agent

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import bpy.stub_internal.rna_enums as rna_enums

bl_info = {
    "name" : "Geometry Script",
    "author" : "Carson Katri",
    "description" : "Python scripting for geometry nodes",
    "blender" : (3, 0, 0),
    "version" : (0, 1, 2),
    "location" : "",
    "warning" : "",
    "category" : "Node"
}

class TEXT_MT_templates_geometryscript(bpy.types.Menu):
    bl_label = "Geometry Script"

    def draw(self, context):
        self.path_menu(
            [os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")],
            "text.open",
            props_default={"internal": True},
            filter_ext=lambda ext: (ext.lower() == ".py") # type: ignore
        )

class OpenDocumentation(bpy.types.Operator):
    bl_idname = "geometry_script.open_documentation"
    bl_label = "Open Documentation"

    def execute(self, context) -> set["rna_enums.OperatorReturnItems"]:
        documentation_path = Path(__file__).with_name("docs") / "documentation.html"
        webbrowser.open(documentation_path.as_uri())
        return {'FINISHED'}

class GeometryScriptSettings(bpy.types.PropertyGroup):
    auto_resolve: bpy.props.BoolProperty(name="Auto Resolve", default=False, description="If the file is edited externally, automatically accept the changes")

class GeometryScriptMenu(bpy.types.Menu):
    bl_idname = "TEXT_MT_geometryscript"
    bl_label = "Geometry Script"

    def draw(self, context):
        assert context is not None

        layout = self.layout
        assert layout is not None

        text = context.space_data.text
        if text and len(text.filepath) > 0:
            layout.prop(context.scene.geometry_script_settings, 'auto_resolve')
        layout.operator(OpenDocumentation.bl_idname)

def templates_menu_draw(self, context):
    self.layout.menu(TEXT_MT_templates_geometryscript.__name__)

def editor_header_draw(self, context):
    self.layout.menu(GeometryScriptMenu.bl_idname)

def auto_resolve():
    if bpy.context.scene.geometry_script_settings.auto_resolve:
        try:
            for area in bpy.context.screen.areas:
                for space in area.spaces:
                    if space.type == 'TEXT_EDITOR':
                        with bpy.context.temp_override(area=area, space=space):
                            text = bpy.context.space_data.text
                            if text and text.is_modified:
                                bpy.ops.text.resolve_conflict(resolution='RELOAD')
                                if bpy.context.space_data.use_live_edit:
                                    # agent.run reports errors and keeps the report for
                                    # agent.status(), where run_script would only fail.
                                    if text.filepath:
                                        agent.run(bpy.path.abspath(text.filepath))
                                    else:
                                        agent.run(text.as_string(), filename=text.name)
        except Exception as error:
            print(f"Geometry Script live edit: {error}")
    return 1

def register():
    bpy.utils.register_class(TEXT_MT_templates_geometryscript)
    bpy.types.TEXT_MT_templates.append(templates_menu_draw) # type: ignore
    bpy.utils.register_class(GeometryScriptSettings)
    bpy.utils.register_class(GeometryScriptPreferences)
    bpy.utils.register_class(OpenDocumentation)
    bpy.utils.register_class(GeometryScriptMenu)

    bpy.types.TEXT_HT_header.append(editor_header_draw) # type: ignore

    bpy.types.Scene.geometry_script_settings = bpy.props.PointerProperty(type=GeometryScriptSettings) # type: ignore

    bpy.app.timers.register(auto_resolve, persistent=True)

def unregister():
    bpy.utils.unregister_class(TEXT_MT_templates_geometryscript)
    bpy.types.TEXT_MT_templates.remove(templates_menu_draw) # type: ignore
    bpy.utils.unregister_class(GeometryScriptSettings)
    bpy.utils.unregister_class(GeometryScriptPreferences)
    bpy.utils.unregister_class(OpenDocumentation)
    bpy.utils.unregister_class(GeometryScriptMenu)
    bpy.types.TEXT_HT_header.remove(editor_header_draw) # type: ignore
    try:
        bpy.app.timers.unregister(auto_resolve)
    except:
        pass
