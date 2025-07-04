from geometry_script import *

@tree("Repeat Grid")
def repeat_grid(geometry: Geometry, columns: Int, rows: Int):
   # measure your geometry’s bounds
    bbox = geometry.bounding_box()
    span_x = bbox.max.x - bbox.min.x
    span_y = bbox.max.y - bbox.min.y

    # total grid size = N * object size
    total_x = columns * span_x
    total_y = rows    * span_y

    # one extra vertex gives N cells
    g = grid(
        size_x=total_x, size_y=total_y,
        vertices_x=columns+1, vertices_y=rows+1
    ).mesh.mesh_to_points()

    return g.instance_on_points(instance=geometry)