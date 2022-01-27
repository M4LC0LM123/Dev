
import pygame

class gameObject:
    def __init__(self, window, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window

    def drawSelf(self):
        pygame.draw.rect()
