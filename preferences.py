import bpy
import sys
import os

class GeometryScriptPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    typeshed_path: bpy.props.StringProperty(
        name="Typeshed Path",
        get=lambda self: os.path.join(os.path.dirname(__file__), 'typeshed'),
        set=lambda self, _: None
    )

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="External Editing", icon="CONSOLE")
        box.label(text="Add the following path to the module lookup paths in your IDE of choice:")
        box.prop(self, "typeshed_path")
        vscode = box.box()
        vscode.label(text="Visual Studio Code", icon="QUESTION")
        vscode.label(text="Setup instructions for the Visual Studio Code:")
        ctrl_cmd = 'CMD' if sys.platform == 'darwin' else 'CTRL'
        vscode.label(text=f"1. Press {ctrl_cmd}+Shift+P")
        vscode.label(text=f"2. Search for 'Preferences: Open Settings (UI)'")
        vscode.label(text=f"3. Search for 'Python > Analysis: Extra Paths")
        vscode.label(text=f"4. Click 'Add Item'")
        vscode.label(text=f"5. Paste the typeshed path from above")
