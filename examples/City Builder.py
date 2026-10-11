# Create a curve object as the base.
# In Edit Mode, use the Draw tool to create new roads in the city.

from geometry_script import *

@tree("City Builder")
def city_builder(
    geometry: Geometry,
    building_size_min: Vector = (0.1, 0.1, 0.2),
    building_size_max: Vector = (0.3, 0.3, 1.0),
    size_x: float = 5.0,
    size_y: float = 5.0,
    road_width: float = 0.25,
    seed: int = 0,
    resolution: int = 60,
):
    # Road geometry from input curves
    road_points = curve_to_points(curve=geometry, mode="EVALUATED").points
    roads = curve_to_mesh(
        curve=geometry,
        profile_curve=curve_line(
            start=(road_width * -0.5, 0.0, 0.0),
            end=(road_width * 0.5, 0.0, 0.0),
        ).curve,
    ).mesh

    # Randomly distribute buildings on a grid
    building_points = distribute_points_on_faces(
        mesh=grid(
            size_x=size_x, size_y=size_y,
            vertices_x=resolution, vertices_y=resolution,
        ).mesh,
        seed=seed,
    ).points

    # Delete building points that are too close to a road
    road_distance = geometry_proximity(
        geometry=road_points,
        target_element="POINTS",
        sample_position=position().position,
    ).distance
    building_points = delete_geometry(
        geometry=building_points,
        domain="POINT",
        selection=compare(a=road_distance, b=road_width * 2, operation="LESS_THAN").result,
    ).geometry

    # Instance a randomly scaled cube on each remaining point
    building = transform_geometry(
        geometry=cube(size=(1.0, 1.0, 1.0)).mesh,
        translation=(0.0, 0.0, 0.5),
    ).geometry
    random_scale = random_value(
        min=building_size_min,
        max=building_size_max,
        seed=seed,
        id=id_().id,
    ).value
    buildings = instance_on_points(
        points=building_points,
        instance=building,
        scale=random_scale,
    ).instances

    return join_geometry(geometry=[roads, buildings]).geometry
