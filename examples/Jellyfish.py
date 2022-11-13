from geometry_script import *

@tree("Jellyfish")
def jellyfish(geometry: Geometry, head_radius: Float):
    curve_points = geometry.curve_to_points(mode='EVALUATED').points
    for i, points in curve_points:
        return instance_on_points()
    head = ico_sphere(radius=head_radius).transform(
        translation=head_transform.position,
        rotation=rotate_euler(space='LOCAL', rotation=align_euler_to_vector(vector=head_transform.tangent), rotate_by=(90, 0, 0)),
        scale=(1, 1, 0.5)
    )
    return join_geometry(geometry=[head, geometry])