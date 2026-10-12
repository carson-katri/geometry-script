from geometry_script import *

@tree("Repeat Grid")
def repeat_grid(
    geometry: Geometry,
    columns: int = 3,
    rows: int = 3,
    spacing_x: float = 0.5,
    spacing_y: float = 0.5,
):
    # Measure the geometry's bounds
    bounds = bounding_box(geometry=geometry)
    size = separate_xyz(vector=bounds.max - bounds.min)

    # Place one grid vertex per copy, one object width (plus spacing) apart
    step_x = size.x + spacing_x
    step_y = size.y + spacing_y
    points = mesh_to_points(
        mesh=grid(
            size_x=(columns - 1) * step_x,
            size_y=(rows - 1) * step_y,
            vertices_x=columns,
            vertices_y=rows,
        ).mesh
    ).points

    return instance_on_points(points=points, instance=geometry).instances
