import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(100, 100), (90, 100), (80, 100)]
direction = (CELL_SIZE, 0)
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, 
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
    
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        print("Game Over!")
        running = False
    
    if new_head == food:
        food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, 
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    else:
        snake.pop()
    
    snake.insert(0, new_head)
    
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()
