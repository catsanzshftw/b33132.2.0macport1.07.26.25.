from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.models.procedural.cylinder import Cylinder
from ursina.models.procedural.cone import Cone

# To fix Panda3D cache permission denied on M1 Mac: Run this in terminal once -> chmod -R u+w ~/Library/Caches/Panda3D-1.10

app = Ursina(borderless=False)  # Helps with window config on Mac
# Explicit size to avoid fractional win-size warnings on high-DPI M1 screen
window.size = Vec2(1440, 935)
window.position = Vec2(180, 117)

# Sky and lighting - normal Mario vibes, bright and cheery
Sky(color=color.azure)
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
# Optional: Add ambient light to brighten shadows
ambient_light = AmbientLight(color=color.rgba(100, 100, 100, 1))  # Adjust intensity if needed

# Large open-world ground - green grass-like (Removed texture)
ground = Entity(model='plane', scale=(500, 1, 500), color=color.green.tint(0.1), collider='box')  # Slightly darker green

# Water moat around castle - blue plane (Removed texture)
moat = Entity(model='plane', scale=(100, 1, 100), y=-0.5, color=color.blue, collider='box')

# Bridge over moat - simple quad (Removed texture)
bridge = Entity(model='quad', scale=(10, 1, 20), position=(0, 0.1, -30), rotation=(90, 0, 0), color=color.brown, collider='box')

# Peach's Castle - blocky build with primitives (Removed texture)
# Main base (Simplified collider potentially)
castle_base = Entity(model='cube', scale=(50, 10, 40), position=(0, 5, 0), color=color.orange, collider='box')

# Towers - using procedural Cylinder (Kept capsule collider for player interaction)
tower1 = Entity(model=Cylinder(resolution=12, height=20, radius=4), position=(-20, 15, -15), color=color.orange, collider='capsule')  # Reduced resolution
tower2 = Entity(model=Cylinder(resolution=12, height=20, radius=4), position=(20, 15, -15), color=color.orange, collider='capsule')
tower3 = Entity(model=Cylinder(resolution=12, height=20, radius=4), position=(-20, 15, 15), color=color.orange, collider='capsule')
tower4 = Entity(model=Cylinder(resolution=12, height=20, radius=4), position=(20, 15, 15), color=color.orange, collider='capsule')

# Central tower taller (Reduced resolution)
central_tower = Entity(model=Cylinder(resolution=12, height=30, radius=5), position=(0, 20, 0), color=color.orange, collider='capsule')

# Roof - using procedural Cone (Mesh collider might be ok, or simplify if needed)
roof = Entity(model=Cone(resolution=12, height=10, radius=6), position=(0, 35, 0), color=color.red, collider='mesh')  # Reduced resolution

# Windows/doors - simple quads for decoration (No change needed, no texture)
door = Entity(model='quad', scale=(5, 8, 1), position=(0, 4, -20.1), color=color.black)
window1 = Entity(model='quad', scale=(3, 3, 1), position=(-10, 8, -20.1), color=color.white)
window2 = Entity(model='quad', scale=(3, 3, 1), position=(10, 8, -20.1), color=color.white)

# Trees around outside - cylinder trunk + sphere leaves (Simplified colliders for leaves)
def make_tree(pos):
    trunk = Entity(model=Cylinder(resolution=6, height=10, radius=1), position=pos, color=color.brown, collider='capsule')  # Reduced resolution
    # Use box or capsule collider for leaves instead of sphere if performance is critical, or remove collider
    leaves = Entity(model='sphere', scale=8, position=pos + (0, 10, 0), color=color.lime, collider='sphere')  # Could consider removing collider

make_tree((-40, 0, -40))
make_tree((40, 0, -40))
make_tree((-40, 0, 40))
make_tree((40, 0, 40))

# Hills for open-world feel (Removed texture)
hill1 = Entity(model='sphere', scale=(20, 10, 20), position=(-60, 5, 0), color=color.green, collider='sphere')
hill2 = Entity(model='sphere', scale=(30, 15, 30), position=(60, 7.5, 0), color=color.green, collider='sphere')

# Backyard behind castle (Removed texture)
back_ground = Entity(model='plane', scale=(100, 1, 100), position=(0, 0, 60), color=color.green, collider='box')
platform1 = Entity(model='cube', scalae=(10, 2, 10), position=(-20, 5, 70), color=color.yellow, collider='box')
platform2 = Entity(model='cube', scale=(10, 2, 10), position=(20, 10, 80), color=color.yellow, collider='box')
platform3 = Entity(model='cube', scale=(15, 2, 15), position=(0, 15, 90), color=color.yellow, collider='box')

# Player controller - Mario-like, first-person for exploration
player = FirstPersonController(position=(0, 2, -50), speed=10, jump_height=5)

# Basic update for open-world feel
def update():
    pass

# EditorCamera()  # Commented out for pure play mode

app.run()
