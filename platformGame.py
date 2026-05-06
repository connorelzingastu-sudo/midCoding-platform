import pgzrun

# Variables
TITLE = "Platform Game"
WIDTH = 800
HEIGHT = 500
player = Rect((100, 400), (40, 40))
velocity_y = 0
gravity = 1
on_ground = False

def draw():
    screen.clear()
    screen.draw.filled_rect(player, "blue")

def update():
    global velocity_y, on_ground

    velocity_y += gravity
    player.y += velocity_y
    
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    if keyboard.space and on_ground:
        velocity_y = -15
        on_ground = False
    
    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

pgzrun.go()
