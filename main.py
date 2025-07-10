import pygame
import sys

# 初始化
pygame.init()
screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 60

# 加载玩家图像
iron_man = pygame.image.load("images/player.png")

# 加载敌人动画帧（原先的 coin/bad guy/enemy 统一视为敌人动画）
enemy_frames = [
    pygame.image.load("images/bad guy-1.png.png"),
    pygame.image.load("images/bad guy-2.png.png"),
    pygame.image.load("images/bad guy-3.png.png"),
    pygame.image.load("images/bad guy-4.png.png")
]
enemy_frame_index = 0
enemy_frame_count = len(enemy_frames)
enemy_anim_timer = 0
enemy_anim_delay = 100  # 每 100 毫秒换一帧
enemy_pos = pygame.Rect(900, 100, 64, 64)  # 敌人坐标和尺寸

# 玩家设置
player_x, player_y = 20, 30
player_width, player_height = 10, 10
player_speed = 15
player = pygame.Rect(player_x, player_y, player_width, player_height)

# 颜色设置
player_color = (95, 235, 128)
bg_color = (0, 0, 0)
text_color = (255, 255, 255)

# 分数系统
score = 0
elapsed = 0
scoring_interval = 1000  # 每 1000 毫秒加分


# 文字绘制函数
def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


# 敌人动画绘制
def draw_enemy():
    global enemy_frame_index, enemy_anim_timer
    enemy_anim_timer += clock.get_time()
    if enemy_anim_timer >= enemy_anim_delay:
        enemy_anim_timer = 0
        enemy_frame_index = (enemy_frame_index + 1) % enemy_frame_count
    screen.blit(enemy_frames[enemy_frame_index], enemy_pos)


# 精灵绘制
def draw_sprites():
    screen.blit(iron_man, player)
    game_font = pygame.font.SysFont("", 30)
    draw_text("Score: " + str(score), game_font, text_color, 10, 10)
    draw_enemy()


# 游戏主循环
while True:
    clock.tick(fps)

    dt = clock.tick(fps) / 1000.0
    elapsed += dt * 1000

    while elapsed >= scoring_interval:
        score += 1000
        elapsed -= scoring_interval

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.y -= player_speed
    elif key[pygame.K_s]:
        player.y += player_speed

    screen.fill(bg_color)
    draw_sprites()
    pygame.display.flip()
