from geometry_script import *
from geometry_script import shader as sh

# A reusable shader node group: stripes between two colors
@sh.shader("Stripes")
def stripes(
    color_a: Color = (0.9, 0.3, 0.1, 1.0),
    color_b: Color = (0.1, 0.1, 0.1, 1.0),
    scale: float = 6.0,
):
    wave = sh.wave_texture(scale=scale, distortion=2.0)
    return sh.mix(data_type="RGBA", factor=wave.factor, a=color_a, b=color_b).result

# A material using the group
@sh.material("Striped")
def striped():
    color = stripes(scale=10.0)
    return sh.principled_bsdf(base_color=color, roughness=0.35).bsdf

# The scene's world
@sh.world("Studio", scene=True)
def studio():
    return sh.background(color=(0.05, 0.06, 0.08, 1.0), strength=1.0).background

# Geometry that uses the material
@tree("Striped Spheres")
def striped_spheres(count: int = 5, radius: float = 0.4):
    points = mesh_to_points(mesh=mesh_line(count=count, offset=(1.0, 0.0, 0.0)).mesh).points
    sphere = uv_sphere(radius=radius).mesh
    spheres = instance_on_points(points=points, instance=sphere).instances
    return set_material(geometry=spheres, material=striped()).geometry
