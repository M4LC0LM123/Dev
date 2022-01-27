
import pygame
import random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#window and state variables
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")
done = False
clock = pygame.time.Clock()
isRunning = True

#player variables
x = 250
y = 250
width = 40
height = 40
vel = 5

#box variables
boxX = 300
boxY = 300
boxCollidingUp = False
boxCollidingDown = False
boxCollidingRight = False
boxCollidingLeft = False
boxColliding = False
outlineX = 40
outlineY = 420

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

    #box colliders
    boxUpCldr = pygame.draw.rect(screen, RED, [boxX + 5, boxY, 30, 15])
    boxDownCldr = pygame.draw.rect(screen, RED, [boxX + 5, boxY + 25, 30, 15])
    boxRightCldr = pygame.draw.rect(screen, RED, [boxX + 25, boxY + 5, 15, 30])
    boxLeftCldr = pygame.draw.rect(screen, RED, [boxX, boxY + 5, 15, 30])

    #walls
    wall = pygame.draw.rect(screen, WHITE, [0, 0, 500, 40])
    wall1 = pygame.draw.rect(screen, WHITE, [0, 500 - 40, 500, 40])
    wall2 = pygame.draw.rect(screen, WHITE, [0, 0, 40, 500])
    wall3 = pygame.draw.rect(screen, WHITE, [500 - 40, 0, 40, 500])

    #boxes
    box = pygame.draw.rect(screen, RED, [boxX, boxY, 40, 40])
    boxOutline = pygame.draw.rect(screen, GREEN, [40, 420, 40, 40], 3)

    #check for collisions
    #player collisions
    if UpCldr.colliderect(wall) or UpCldr.colliderect(box):
        collidingUp = True
    else:
        collidingUp = False

    if DownCldr.colliderect(wall1) or DownCldr.colliderect(box):
        collidingDown = True
    else:
        collidingDown = False

    if RightCldr.colliderect(wall3) or RightCldr.colliderect(box):
        collidingRight = True
    else:
        collidingRight = False

    if LeftCldr.colliderect(wall2) or LeftCldr.colliderect(box):
        collidingLeft = True
    else:
        collidingLeft = False


    #box collisions 
    if boxUpCldr.colliderect(wall):
        boxCollidingUp = True
    else:
        boxCollidingUp = False

    if boxDownCldr.colliderect(wall1):
        boxCollidingDown = True
    else:
        boxCollidingDown = False

    if boxRightCldr.colliderect(wall3):
        boxCollidingRight = True
    else:
        boxCollidingRight = False

    if boxLeftCldr.colliderect(wall2):
        boxCollidingLeft = True
    else:
        boxCollidingLeft = False

    if boxColliding == False:
        if boxCollidingUp == False:
            if UpCldr.colliderect(box):
                boxY -= vel
        
        if boxCollidingDown == False:
            if DownCldr.colliderect(box):
                boxY += vel

        if boxCollidingRight == False:        
            if RightCldr.colliderect(box):
                boxX += vel
        
        if boxCollidingLeft == False:
            if LeftCldr.colliderect(box):
                boxX -= vel
    
    if box.colliderect(boxOutline):
        boxX = outlineX
        boxY = outlineY
        isRunning = False
        if keys[pygame.K_r]:
            isRunning = True
        if isRunning == True:
            x = 300
            y = 300
            boxX = 250
            boxY = 250

    if isRunning == False:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("U WON", True, (255,255,255))
        screen.blit(text, (200, 225))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()