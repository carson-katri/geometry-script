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

import bpy
import os

from .tree import *

bl_info = {
    "name" : "Geometry Script",
    "author" : "Carson Katri",
    "description" : "Python scripting for geometry nodes",
    "blender" : (3, 0, 0),
    "version" : (0, 1, 0),
    "location" : "",
    "warning" : "",
    "category" : "Node"
}

class TEXT_MT_templates_geometryscript(bpy.types.Menu):
    bl_label = "Geometry Script"

    def draw(self, _context):
        self.path_menu(
            [os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")],
            "text.open",
            props_default={"internal": True},
            filter_ext=lambda ext: (ext.lower() == ".py")
        )

def templates_menu_draw(self, context):
    self.layout.menu(TEXT_MT_templates_geometryscript.__name__)

def register():
    bpy.utils.register_class(TEXT_MT_templates_geometryscript)
    bpy.types.TEXT_MT_templates.append(templates_menu_draw)

def unregister():
    bpy.utils.unregister_class(TEXT_MT_templates_geometryscript)
    bpy.types.TEXT_MT_templates.remove(templates_menu_draw)