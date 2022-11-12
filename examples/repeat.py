from geometry_script import *

@tree
def repeat(size: Vector):
    cubes = []
    for x in range(5):
        for y in range(5):
            for z in range(5):
                c = cube(size=(0.1, 0.1, 0.1))
                cubes.append(c.transform(translation=(x, y, z)))
    return join_geometry(geometry=cubes)