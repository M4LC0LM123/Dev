
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
y = 400
width = 40
height = 40
vel = 2

wallX = 0
wallY = random.randint(-40, 40)
wallY2 = random.randint(-40, 40)
wallWidth = random.randint(150, 200)
wallWidth2 = random.randint(150, 200)
wallHeight = 40
wallVel = 0
wallVelMax = 100

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
        
    screen.fill(BLACK)

    wallVel += 0.01

    if wallVel >= wallVelMax:
        wallVel = 50

    wallY += wallVel
    wallY2 += wallVel

    if wallY >= 500:
        wallY = random.randint(-40, 40)
        wallWidth = random.randint(150, 200)
    
    if wallY2 >= 500:
        wallY2 = random.randint(-40, 40)
        wallWidth2 = random.randint(150, 200)

    player = pygame.draw.rect(screen, GREEN, [x - width, y - height, width, height])
    wall = pygame.draw.rect(screen, RED, [wallX, wallY, wallWidth, wallHeight], 0)
    wall2 = pygame.draw.rect(screen, RED, [500 - wallWidth, wallY2, wallWidth2, wallHeight], 0)

    if player.colliderect(wall):
        width = 0
        height = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit