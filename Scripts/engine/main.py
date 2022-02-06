from tkinter import *
import pygame

root = Tk()

runBtn = Button(root, text="Run")
runBtn.place(250, 250, 40, 40)

def main():
    pygame.init() #initialize pygame
    SCREEN_WIDTH = 600 # width (in px)
    SCREEN_HEIGHT = 800 # height (in px)

    WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates a screen of 600px X 800px

    while True:
        pygame.display.update() # updates the screen

root.geometry("500x500")
root.mainloop()
input()