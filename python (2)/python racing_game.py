
from ursina import *
from random import randint

app = Ursina()

window.title = "Ultimate 3D Racing Game"
window.color = color.rgb(100, 180, 255)

# Road
road = Entity(
    model='cube',
    color=color.dark_gray,
    scale=(12, 0.2, 100),
    position=(0, -0.2, 10)
)

# Road markings
lines = []
for z in range(-30, 60, 8):
    line = Entity(
        model='cube',
        color=color.white,
        scale=(0.15, 0.03, 3),
        position=(0, -0.08, z)
    )
    lines.append(line)

# Player car
car = Entity(
    model='cube',
    color=color.red,
    scale=(1.5, 0.8, 3),
    position=(0, 0.5, -5)
)

# Car roof
Entity(
    parent=car,
    model='cube',
    color=color.black,
    scale=(0.7, 0.7, 0.65),
    position=(0, 0.8, 0)
)

# Traffic cars
traffic = []

for i in range(5):
    enemy = Entity(
        model='cube',
        color=color.azure,
        scale=(1.5, 1, 2.5),
        position=(randint(-4, 4), 0.5, i * 15 + 15)
    )
    traffic.append(enemy)

# Game information
score = 0
speed = 15
game_over = False

score_text = Text(
    text="SCORE: 0",
    position=(-0.85, 0.45),
    scale=2
)

speed_text = Text(
    text="SPEED: 15",
    position=(0.5, 0.45),
    scale=2
)

message = Text(
    text="",
    origin=(0, 0),
    scale=3,
    color=color.red
)

# Camera
camera.position = (0, 7, -15)
camera.rotation_x = 20

def update():
    global score, speed, game_over

    if game_over:
        return

    # Car movement
    if held_keys['a'] or held_keys['left arrow']:
        car.x -= 6 * time.dt

    if held_keys['d'] or held_keys['right arrow']:
        car.x += 6 * time.dt

    car.x = max(-4.5, min(4.5, car.x))

    # Increase speed
    speed += time.dt * 0.15

    # Move road markings
    for line in lines:
        line.z -= speed * time.dt
        if line.z < -20:
            line.z += 80

    # Move traffic
    for enemy in traffic:
        enemy.z -= speed * time.dt

        if enemy.z < -15:
            enemy.z = randint(45, 80)
            enemy.x = randint(-4, 4)
            score += 10

        # Check whether the cars overlap on the road's X/Z plane.
        overlaps_x = abs(car.x - enemy.x) < (car.scale_x + enemy.scale_x) / 2
        overlaps_z = abs(car.z - enemy.z) < (car.scale_z + enemy.scale_z) / 2
        if overlaps_x and overlaps_z:
            game_over = True
            message.text = "GAME OVER!"

    score_text.text = "SCORE: " + str(score)
    speed_text.text = "SPEED: " + str(int(speed))

def input(key):
    if key == 'r' and game_over:
        application.restart()

# Lighting
DirectionalLight().look_at(Vec3(1, -1, -1))
AmbientLight(color=color.rgba(120, 120, 120, 0.5))

Sky()

# Instructions
Text(
    text="A / D or LEFT / RIGHT to Drive",
    position=(-0.5, -0.45),
    scale=1.2
)

app.run()
