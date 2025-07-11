
import pygame
import sys

# --- Initialization ---
pygame.init()
screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 60

# --- Colors ---
player_color = (95, 235, 128)
bg_color = (0, 0, 0)
text_color = (255, 255, 255)

# --- Score Settings ---
score = 0
elapsed = 0
scoring_interval = 1000  # Add 1000 points every 1000 milliseconds

# --- Load Images ---
iron_man = pygame.image.load("images/player.png")

enemy_frames = [
    pygame.image.load("images/bad guy-1.png.png"),
    pygame.image.load("images/bad guy-2.png.png"),
    pygame.image.load("images/bad guy-3.png.png"),
    pygame.image.load("images/bad guy-4.png.png")
]

fireball_image = pygame.image.load("images/coin.png")

# --- Enemy Animation Settings ---
enemy_frame_index = 0
enemy_frame_count = len(enemy_frames)
enemy_anim_timer = 0
enemy_anim_delay = 100  # Change frame every 100 milliseconds
enemy_pos = pygame.Rect(900, 100, 64, 64)

# --- Player Settings ---
player_x, player_y = 20, 30
player_width, player_height = 10, 10
player_speed = 15
player = pygame.Rect(player_x, player_y, player_width, player_height)

# --- Fireball Settings ---
fireballs = []
fireball_speed = 8
fireball_timer = 0
fireball_interval = 1000  # Fireball shoots every 1000 milliseconds

# --- Functions ---

# Draw text on screen
def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

# Draw the animated enemy
def draw_enemy():
    global enemy_frame_index, enemy_anim_timer
    enemy_anim_timer += clock.get_time()
    if enemy_anim_timer >= enemy_anim_delay:
        enemy_anim_timer = 0
        enemy_frame_index = (enemy_frame_index + 1) % enemy_frame_count
    screen.blit(enemy_frames[enemy_frame_index], enemy_pos)

# Spawn a new fireball from the enemy position
def spawn_fireball():
    x = enemy_pos.left
    y = enemy_pos.top + enemy_pos.height // 2 - fireball_image.get_height() // 2
    rect = pygame.Rect(x, y, fireball_image.get_width(), fireball_image.get_height())
    fireballs.append(rect)

# Update and draw fireballs
def update_fireballs():
    for fireball in fireballs:
        fireball.x -= fireball_speed
    # Remove fireballs that go off-screen
    fireballs[:] = [fb for fb in fireballs if fb.right > 0]

    # Draw all fireballs
    for fireball in fireballs:
        screen.blit(fireball_image, fireball)

# Draw all game sprites
def draw_sprites():
    screen.blit(iron_man, player)
    game_font = pygame.font.SysFont("", 30)
    draw_text("Score: " + str(score), game_font, text_color, 10, 10)
    draw_enemy()
    update_fireballs()

# --- Game Loop ---
while True:
    clock.tick(fps)

    dt = clock.tick(fps) / 1000.0
    elapsed += dt * 1000

    # Increase score every scoring interval
    while elapsed >= scoring_interval:
        score += 1000
        elapsed -= scoring_interval

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Move player
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.y -= player_speed
    elif key[pygame.K_s]:
        player.y += player_speed

    # Fireball spawn logic
    fireball_timer += clock.get_time()
    if fireball_timer >= fireball_interval:
        fireball_timer = 0
        spawn_fireball()

    # Draw everything
    screen.fill(bg_color)
    draw_sprites()
    pygame.display.flip()
