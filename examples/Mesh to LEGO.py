# NOTE: This example requires Blender 3.4+

from geometry_script import *

@tree("LEGO")
def lego(size: Vector, stud_radius: Float, stud_depth: Float, count_x: Int, count_y: Int):
    base = cube(size=size)
    stud_shape = cylinder(fill_type='NGON', radius=stud_radius, depth=stud_depth, vertices=8).mesh
    stud = stud_shape.transform(translation=combine_xyz(z=(stud_depth / 2) + (size.z / 2)))
    hole = stud_shape.transform(translation=combine_xyz(z=(stud_depth / 2) - (size.z / 2)))
    segment = mesh_boolean(
        operation='DIFFERENCE',
        mesh_1=mesh_boolean(operation='UNION', mesh_2=[base, stud]).mesh,
        mesh_2=hole
    ).mesh
    return mesh_line(count=count_x, offset=(1, 0, 0)).instance_on_points(
        instance=mesh_line(count=count_y, offset=(0, 1, 0)).instance_on_points(instance=segment)
    ).realize_instances().merge_by_distance()

@tree("Mesh to LEGO")
def mesh_to_lego(geometry: Geometry, resolution: Float=0.2):
    return geometry.mesh_to_volume(interior_band_width=resolution, fill_volume=False).distribute_points_in_volume(
        mode='DENSITY_GRID',
        spacing=resolution
    ).instance_on_points(
        instance=lego(size=resolution, stud_radius=resolution / 3, stud_depth=resolution / 8, count_x=1, count_y=1)
    ).realize_instances().merge_by_distance()