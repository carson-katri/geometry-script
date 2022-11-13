import bpy
import os

def load(filename):
    """
    Execute an external script.
    """
    filepath = os.path.join(os.path.dirname(bpy.data.filepath), filename)
    global_namespace = {"__file__": filepath, "__name__": "__main__"}
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), global_namespace)