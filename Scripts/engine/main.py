from tkinter import *
import pygame
from sprite import *

root = Tk()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (105,105,105)

def main():
    pygame.init()

    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Game")

    x = 50
    y = 50
    width = 40
    height = 40
    vel = 2

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= vel

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += vel

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= vel

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += vel
        
        screen.fill((0,0,0))
        player = drawSprite(screen, GREEN, x, y, width, height)  
        player.drawSelf()
        wall = drawSprite(screen, WHITE, 250, 250, width, height)
        wall.drawSelf()
        
        pygame.display.update() 
        


runBtn = Button(root, text="Run", command=main)
runBtn.place(x = 220, y = 210, width=60, height=40)

root.geometry("500x500")
root.mainloop()
pygame.quit()
input()