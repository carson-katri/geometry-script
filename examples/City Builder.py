# Create a curve object as the base.
# In Edit Mode, use the Draw tool to create new roads in the city.

from geometry_script import *

@tree("City Builder")
def city_builder(
    geometry: Geometry,
    building_size_min: Vector = (0.1, 0.1, 0.2),
    building_size_max: Vector = (0.3, 0.3, 1),
    size_x: Float = 5.0,
    size_y: Float = 5.0,
    road_width: Float = 0.25,
    seed: Int = 0,
    resolution: Int = 60
):
    # Road geometry from input curves
    road_points = geometry.curve_to_points().points
    yield geometry.curve_to_mesh(
        profile_curve=curve_line(
            start=combine_xyz(x=road_width * -0.5),
            end=combine_xyz(x=road_width / 2)
        )
    )

    # Randomly distribute buildings on a grid
    building_points = grid(
        size_x=size_x, size_y=size_y,
        vertices_x=resolution, vertices_y=resolution
    ).distribute_points_on_faces(
        seed=seed
    # Delete invalid building points based on proximity to a road
    ).points.delete_geometry(
        domain=DeleteGeometry.Domain.POINT,
        selection=road_points.geometry_proximity(target_element=GeometryProximity.TargetElement.POINTS, source_position=position()).distance < road_width * 2
    )
    random_scale = random_value(data_type=RandomValue.DataType.FLOAT_VECTOR, min=building_size_min, max=building_size_max, seed=seed + id())
    yield building_points.instance_on_points(
        instance=cube(size=(1, 1, 1)).transform(translation=(0, 0, 0.5)),
        scale=random_scale
    )