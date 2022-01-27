
from ast import walk
from queue import Empty
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

#player variables
x = 250
y = 250
width = 40
height = 40
vel = 5

#collision variables
collidingLeft = False
collidingRight = False
collidingUp = False
collidingDown = False


#update 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    #Player Movement
    keys = pygame.key.get_pressed()
    
    if collidingLeft == False:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= vel

    if collidingRight == False:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += vel

    if collidingUp == False:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= vel

    if collidingDown == False:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += vel

        
    screen.fill(BLACK)

    #draw sprites/colliders
    player = pygame.draw.rect(screen, GREEN, [x, y, width, height])
    UpCldr = pygame.draw.rect(screen, GREEN, [x + 5, y, 30, 15])
    DownCldr = pygame.draw.rect(screen, GREEN, [x + 5, y + 25, 30, 15])
    RightCldr = pygame.draw.rect(screen, GREEN, [x + 25, y + 5, 15, 30])
    LeftCldr = pygame.draw.rect(screen, GREEN, [x, y + 5, 15, 30])
    wall = pygame.draw.rect(screen, WHITE, [0, 0, 500, 40])
    wall1 = pygame.draw.rect(screen, WHITE, [0, 500 - 40, 500, 40])
    wall2 = pygame.draw.rect(screen, WHITE, [0, 0, 40, 500])
    wall3 = pygame.draw.rect(screen, WHITE, [500 - 40, 0, 40, 500])

    #check for collisions
    if UpCldr.colliderect(wall) or UpCldr.colliderect(wall1):
        collidingUp = True
    else:
        collidingUp = False

    if DownCldr.colliderect(wall) or DownCldr.colliderect(wall1):
        collidingDown = True
    else:
        collidingDown = False

    if RightCldr.colliderect(wall) or RightCldr.colliderect(wall3):
        collidingRight = True
    else:
        collidingRight = False

    if LeftCldr.colliderect(wall) or LeftCldr.colliderect(wall2):
        collidingLeft = True
    else:
        collidingLeft = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit