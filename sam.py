import pygame
import sys

# Initialize PyGame
pygame.init()

# Screen setup
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 24

# Title & Icon
pygame.display.set_caption("Samuel T")
icon = pygame.image.load('images/Blush.BoB.png')
pygame.display.set_icon(icon)

# Load images
background = pygame.transform.scale(pygame.image.load('images/background.png'), (screen_width, screen_height))
player_image = pygame.image.load("images/character.png")
sword_player_image = pygame.image.load("images/swword person.png")  # Check spelling of "sword"
enemy_image = pygame.image.load("images/Bob.png")
coin_image = pygame.image.load("images/coin.png")
sword_image = pygame.image.load("images/swword.png")
goal_image = pygame.image.load("images/goal.png")

# Font and colors
game_font = pygame.font.SysFont("", 30)
text_color = (255, 255, 255)
UI_color = (0, 0, 0)
bg_color = (45, 76, 180)

# Player properties
player_x = 10
player_y = 40
player_width = 64
player_height = 64
player_speed = 15
score = 0
has_sword = False
game_scene = "level"

# Rects
player = pygame.Rect(player_x, player_y, player_width, player_height)
enemy = pygame.Rect(500, 100, 64, 64)
enemy_speed = 3
enemy_direction = 1  # 1 = right, -1 = left

coins = [
    pygame.Rect(300, 100, coin_image.get_width(), coin_image.get_height()),
    pygame.Rect(400, 200, coin_image.get_width(), coin_image.get_height()),
    pygame.Rect(500, 300, coin_image.get_width(), coin_image.get_height())
]
swords = [
    pygame.Rect(130, 150, 64, 64),
    pygame.Rect(500, 400, 64, 64)
]
goal = pygame.Rect(450, 200, goal_image.get_width(), goal_image.get_height())
score_ui = pygame.Rect(0, 0, screen_width, 40)

# Draw text
def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

# Draw game sprites
def draw_sprites():
    # Player with or without sword
    current_player_image = sword_player_image if has_sword else player_image
    screen.blit(current_player_image, player)

    # Show swords (if not yet picked up)
    if not has_sword:
        for sword in swords:
            screen.blit(sword_image, sword)

    draw_enemies()
    draw_coins()
    draw_swords()

    # UI bar + Score
    pygame.draw.rect(screen, UI_color, score_ui)
    draw_text("Score: " + str(score), game_font, text_color, 10, 10)

    # Goal
    screen.blit(goal_image, goal)
    if player.colliderect(goal):
        global game_scene
        game_scene = "you_win"

def draw_enemies():
    screen.blit(enemy_image, enemy)
    if player.colliderect(enemy):
        pygame.quit()
        sys.exit()

def draw_coins():
    global score
    for coin in coins[:]:
        screen.blit(coin_image, (coin.x, coin.y))
        if coin.colliderect(player):
            coins.remove(coin)
            score += 1

def draw_swords():
    global has_sword, score
    for sword in swords[:]:
        if player.colliderect(sword):
            swords.remove(sword)
            score += 5
            has_sword = True

# ========================
#         MAIN LOOP
# ========================
while True:
    clock.tick(fps)

    # Enemy movement (left ↔ right)
    enemy.x += enemy_speed * enemy_direction
    if enemy.right >= screen_width or enemy.left <= 0:
        enemy_direction *= -1  # Reverse direction

    # Sword pickup check
    for sword in swords:
        if not has_sword and player.colliderect(sword):
            has_sword = True

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.move_ip(player_speed, 0)
        if player.x >= screen_width - player_width:
            player.x = screen_width - player_width
    elif keys[pygame.K_a]:
        player.move_ip(-player_speed, 0)
        if player.x <= 0:
            player.x = 0
    elif keys[pygame.K_w]:
        player.move_ip(0, -player_speed)
        if player.y <= player_height / 2:
            player.y = player_height / 2
    elif keys[pygame.K_s]:
        player.move_ip(0, player_speed)
        if player.y >= screen_height - player_height:
            player.y = screen_height - player_height

    # Draw scenes
    if game_scene == "level":
        screen.blit(background, (0, 0))
        draw_sprites()
    elif game_scene == "title":
        screen.fill((133, 12, 176))
    elif game_scene == "game_over":
        screen.fill((255, 0, 0))
    elif game_scene == "you_win":
        screen.fill((0, 0, 0))
        draw_text("YOU WIN!", game_font, text_color, screen_width // 2 - 60, screen_height // 2)

    pygame.display.flip()
