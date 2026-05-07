import pgzrun

# Variables
TITLE = "Platform Game"
WIDTH = 800
HEIGHT = 500
win = False

# Player Variables
player = Rect((100, 400), (40, 40))
velocity_y = 0
gravity = 1
on_ground = False
power_jump = False

platforms = [
    Rect((0,   470),(800, 30)),
    Rect((200, 380),(150, 20)),
    Rect((450, 300),(150, 20)),
    Rect((650, 220),(100, 20))
]

hidden_platforms = [
    Rect((100,   260),(30, 30)),
]

# Collectibles
diamonds = [
    Rect((250, 340), (20, 20)),
    Rect((500, 260), (20, 20)), 
    Rect((660, 180), (20, 20)), 
    Rect((720, 180), (20, 20))
]

special_diamonds = [
    Rect ((40, 120),  (20, 20)), 
]
score = 0

# Goals and Hazards
door = Rect((740,0),(40,60))

# Collisions
def door_collision():
    global win
    if player.colliderect(door):
        win = True

def diamond_collision():
    global score
    for diamond in diamonds[ : ]:
        if player.colliderect(diamond):
            diamonds.remove(diamond)
            score += 1

    for diamond in special_diamonds[ : ]:
        if player.colliderect(diamond):
            special_diamonds.remove(diamond)
            score += 1000

def platform_collision():
    global velocity_y, on_ground

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

    for platform in hidden_platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

def collision_check():
    diamond_collision()
    platform_collision()
    door_collision()

# Drawing
def draw_platforms():
    for platform in platforms:
        screen.draw.filled_rect(platform, "Brown")

def draw_player():
    screen.draw.filled_rect(player, "Lime Green")

def draw_diamonds():
    for diamond in diamonds:
        screen.draw.filled_rect(diamond, "Light Blue")

    for diamond in special_diamonds:
        screen.draw.filled_rect(diamond, "Blue")

def draw():
    screen.clear()
    if win:
        screen.draw.text("Congratulations You Won!!!!", (160, 300), fontsize=50, color="Green")
    else:
        draw_platforms()
        screen.draw.filled_rect(door, "White")
        draw_diamonds()
        draw_player()
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
        if power_jump:
            screen.draw.text(f"Super Bounce Activated", (10, 50), fontsize=30, color="white")
    
# Update state
def update():
    global velocity_y, on_ground, power_jump

    velocity_y += gravity
    player.y += velocity_y
    
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    if keyboard.space and on_ground:
        velocity_y = -30 if power_jump else -15
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

    if score > 1000:
        power_jump = True

pgzrun.go()
