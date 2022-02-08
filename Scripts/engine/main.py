
from tkinter import *
import pygame
from sprite import *

root = Tk()

fps = 60

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (105,105,105)

weapons = []

def main():
    pygame.init()

    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Game")

    pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    gravity = 5
    gravity2 = 5

    isRunning = False

    #player variables
    x1 = 50
    y1 = 50
    x2 = 450
    y2 = 50
    width = 40
    height = 40
    vel = 4
    jumpForce = 10
    air_timer = 0
    air_timer2 = 0

    collidingLeft = False
    collidingRight = False
    collidingUp = False
    collidingDown = False

    collidingLeft2 = False
    collidingRight2 = False
    collidingUp2 = False
    collidingDown2 = False

    playerOneTurn = True
    playerTwoTurn = False

    run = True
    clock = pygame.time.Clock()
    

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        y1 += gravity
        y2 += gravity2

        mouse_x, mouse_y = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_1]:
            playerOneTurn = True
            playerTwoTurn = False

        if keys[pygame.K_2]:
                playerOneTurn = False
                playerTwoTurn = True
            

        if playerOneTurn == True:
            if collidingLeft == False:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    x1 -= vel

            if collidingRight == False:
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    x1 += vel

            if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if air_timer < 20:
                        y1 -= jumpForce

            if isRunning == True:
                if keys[pygame.K_LCTRL] or pygame.mouse.get_pressed()[0]:
                    weapons.append((mouse_x, mouse_y, 20, 20))

        if playerTwoTurn == True:
            if collidingLeft2 == False:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    x2 -= vel

            if collidingRight2 == False:
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    x2 += vel

            if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if air_timer2 < 20:
                        y2 -= jumpForce

            if isRunning == True:
                if keys[pygame.K_LCTRL] or pygame.mouse.get_pressed()[0]:
                    weapons.append((mouse_x, mouse_y, 20, 20))

        if keys[pygame.K_ESCAPE]:
            isRunning = False

        screen.fill((BLACK))        

        for weapon in weapons:
            pygame.draw.rect(screen, WHITE, weapon)

        if isRunning == True:

            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            #players
            playerOne = pygame.draw.rect(screen, BLUE, (x1, y1, width, height))  
            playerTwo = pygame.draw.rect(screen, RED, (x2, y2, width, height))  
            #playerOne.drawSelf()

            #draw player one colliders
            UpCldr = pygame.draw.rect(screen, GREEN, (x1 + 5, y1, 30, 15))
            DownCldr = pygame.draw.rect(screen, GREEN, (x1 + 5, y1 + 25, 30, 15))
            RightCldr = pygame.draw.rect(screen, GREEN, (x1 + 25, y1 + 5, 15, 30))
            LeftCldr = pygame.draw.rect(screen, GREEN, (x1, y1 + 5, 15, 30))

            #draw player two colliders
            UpCldr2 = pygame.draw.rect(screen, GREEN, (x2 + 5, y2, 30, 15))
            DownCldr2 = pygame.draw.rect(screen, GREEN, (x2 + 5, y2 + 25, 30, 15))
            RightCldr2 = pygame.draw.rect(screen, GREEN, (x2 + 25, y2 + 5, 15, 30))
            LeftCldr2 = pygame.draw.rect(screen, GREEN, (x2, y2 + 5, 15, 30))

            #walls
            wall = pygame.draw.rect(screen, WHITE, (250, 500 - height, 500, height))
            wall2 = pygame.draw.rect(screen, WHITE, (250, 420, width, height))
            wall3 = pygame.draw.rect(screen, WHITE, (750 - width, 420, width, height))
            wall4 = pygame.draw.rect(screen, WHITE, (800, 500 - height, 150, height))
            wall5 = pygame.draw.rect(screen, WHITE, (50, 500 - height, 150, height))
            #wall.drawSelf()
        
            #check for player one collisions
            if DownCldr.colliderect(wall) or DownCldr.colliderect(wall2) or DownCldr.colliderect(wall3)  or DownCldr.colliderect(wall4) or DownCldr.colliderect(wall5):
                gravity = 0
                air_timer = 0
            else:
                gravity = 5
                air_timer += 1

            if LeftCldr.colliderect(wall2) or LeftCldr.colliderect(wall4):
                collidingLeft = True
            else:
                collidingLeft = False

            if RightCldr.colliderect(wall3):
                collidingRight = True
            else:
                collidingRight = False

            #check for player two collisions
            if DownCldr2.colliderect(wall) or DownCldr2.colliderect(wall2) or DownCldr2.colliderect(wall3) or DownCldr2.colliderect(wall4) or DownCldr2.colliderect(wall5):
                gravity2 = 0
                air_timer2 = 0
            else:
                gravity2 = 5
                air_timer2 += 1

            if LeftCldr2.colliderect(wall2) or LeftCldr2.colliderect(wall4):
                collidingLeft2 = True
            else:
                collidingLeft2 = False

            if RightCldr2.colliderect(wall3):
                collidingRight2 = True
            else:
                collidingRight2 = False

        if isRunning == False:
            startBtn = pygame.draw.rect(screen, WHITE, (500 - 30, 300 - 20, 60, 40))
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)

            x1 = 50
            y1 = 50
            x2 = 450
            y2 = 50

            weapons.clear()

            if pygame.mouse.get_pressed()[0]:
                if startBtn.collidepoint(pygame.mouse.get_pos()):
                    isRunning = True



        pygame.display.flip()
        pygame.display.update() 
        

def Close():
    pygame.quit()


runBtn = Button(root, text="Run", command=main)
runBtn.place(x = 220, y = 210, width=60, height=40)

closeBtn = Button(root, text="Close", command=Close)
closeBtn.place(x = 220, y = 260, width=60, height=40)

root.geometry("500x500")
root.mainloop()
pygame.quit()
input()