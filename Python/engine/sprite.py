import pygame

class drawSprite:
    def __init__(self, screen, color, x, y, width, height):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height



    def drawSelf(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))


