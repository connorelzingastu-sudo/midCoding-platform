import pgzrun

# Variables
TITLE = "Platform Game"
WIDTH = 800
HEIGHT = 500
player = Rect((100, 400), (40, 40))
velocity_y = 0
gravity = 1
on_ground = False

platforms = [
    Rect((0,   470),(800, 30)),
    Rect((200, 380),(150, 20)),
    Rect((450, 300),(150, 20)),
    Rect((650, 220),(100, 20))
]

#diamonds = [
#    Rect ((250 , 340))
#]
def draw_platforms():
    for platform in platforms:
        screen.draw.filled_rect(platform, "Brown")

def draw_player():
    screen.draw.filled_rect(player, "Lime Green")

def draw():
    screen.clear()
    draw_platforms()
    draw_player()

def collision_check():
    global velocity_y, on_ground

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

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

    collision_check()

pgzrun.go()
