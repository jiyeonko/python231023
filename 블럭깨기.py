#cmd
#pip install pygame

import pygame
import sys

# 초기화
pygame.init()

# 게임 설정
WIDTH, HEIGHT = 600, 400
BALL_SPEED = [5, 5]
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10

# 화면 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 패들 초기 위치
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 초기 위치
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# 블록 초기 설정
bricks = []
for i in range(5):
    for j in range(5):
        brick = pygame.Rect(i * 100 + 50, j * 40 + 50, 80, 30)
        bricks.append(brick)

# 게임 루프
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += PADDLE_SPEED

    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]

    # 공과 패들 충돌 처리
    if ball.colliderect(paddle):
        BALL_SPEED[1] = -BALL_SPEED[1]

    # 공과 벽면 충돌 처리
    if ball.left < 0 or ball.right > WIDTH:
        BALL_SPEED[0] = -BALL_SPEED[0]
    if ball.top < 0:
        BALL_SPEED[1] = -BALL_SPEED[1]

    # 공과 블록 충돌 처리
    for brick in bricks:
        if ball.colliderect(brick):
            BALL_SPEED[1] = -BALL_SPEED[1]
            bricks.remove(brick)
            break

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, ball)
    pygame.draw.rect(screen, RED, paddle)

    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
