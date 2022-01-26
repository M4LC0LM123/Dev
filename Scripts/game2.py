import pygame
import random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (105,105,105)

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

pygame.display.set_caption("game")

done = False

clock = pygame.time.Clock()

x = 100
y = 400
width = 40
height = 40
vel = 2
health = 300

healthUpX = random.randint(0, 500 - 40)
healthUpY = random.randint(40, 500 - 40)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= vel

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += vel
        
    screen.fill(GREY)

    health -= 1

    player = pygame.draw.rect(screen, GREEN, [x - width, y - height, width, height])
    healthUp = pygame.draw.rect(screen, WHITE, [healthUpX, healthUpY, 40, 40])
    wall = pygame.draw.rect(screen, WHITE, [0, 0, 500, 40])
    healthBar = pygame.draw.rect(screen, RED, [0, 0, health, 40])

    if health <= 0:
        width = 0
        height = 0

    if player.colliderect(healthUp):
        health = 300
        healthUpX = random.randint(0, 500 - 40)
        healthUpY = random.randint(40, 500 - 40)

    pygame.display.flip()
    clock.tick(60)

pygame.quit