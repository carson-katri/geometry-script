from geometry_script import *

@tree("LEGO")
def lego(
    size: Vector = (1.0, 1.0, 1.0),
    stud_radius: float = 0.3,
    stud_depth: float = 0.2,
    count_x: int = 1,
    count_y: int = 1,
):
    height = separate_xyz(vector=size).z
    base = cube(size=size).mesh
    stud_shape = cylinder(fill_type="NGON", radius=stud_radius, depth=stud_depth, vertices=8).mesh
    stud = transform_geometry(
        geometry=stud_shape, translation=(0.0, 0.0, stud_depth / 2 + height / 2)
    ).geometry
    hole = transform_geometry(
        geometry=stud_shape, translation=(0.0, 0.0, stud_depth / 2 - height / 2)
    ).geometry
    segment = mesh_boolean(
        operation="DIFFERENCE",
        mesh_1=mesh_boolean(operation="UNION", mesh=[base, stud]).mesh,
        mesh_2=[hole],
    ).mesh
    row = instance_on_points(
        points=mesh_line(count=count_y, offset=(0.0, 1.0, 0.0)).mesh,
        instance=segment,
    ).instances
    brick = instance_on_points(
        points=mesh_line(count=count_x, offset=(1.0, 0.0, 0.0)).mesh,
        instance=row,
    ).instances
    return merge_by_distance(geometry=realize_instances(geometry=brick).geometry).geometry

@tree("Mesh to LEGO")
def mesh_to_lego(geometry: Geometry, resolution: float = 0.2):
    volume = mesh_to_volume(mesh=geometry, interior_band_width=resolution).volume
    points = distribute_points_in_volume(
        volume=volume,
        mode="Grid",
        spacing=(resolution, resolution, resolution),
    ).points
    brick = lego(
        (resolution, resolution, resolution),
        resolution / 3,
        resolution / 8,
        1,
        1,
    )
    voxels = instance_on_points(points=points, instance=brick).instances
    return merge_by_distance(geometry=realize_instances(geometry=voxels).geometry).geometry
