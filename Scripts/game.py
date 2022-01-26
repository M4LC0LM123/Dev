
import pygame
import random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("game")

done = False

clock = pygame.time.Clock()

x = 100
y = 450
width = 40
height = 40
vel = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_SPACE]:
        pygame.draw.rect(screen, RED, [5, 5, 20, 20])
        
    screen.fill(BLACK)

    player = pygame.draw.rect(screen, GREEN, [x - width, y - height, width, height])

    pygame.display.flip()
    clock.tick(60)

pygame.quit