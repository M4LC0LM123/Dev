
from tkinter import*
from turtle import*
import turtle

root = Tk()
root.configure(background="#5F5F5F")

#tu pisi sranja
def forward():
    fd(100)

def backward():
    bk(100)
    
def left():
    lt(90)
    fd(100)

def right():
    rt(90)
    fd(100)

def upRight():
    rt(45)
    fd(100)

def downRight():
    rt(-45)
    bk(100)

def upLeft():
    lt(45)
    fd(100)

def downLeft():
    lt(-45)
    bk(100)

def Clear():
    turtle.clearscreen()

def up():
    penup()
    upButton.destroy()
    downButton = Button(root, text='U/D', bg = "#00F7FF",command=down)
    downButton.place(x = 125, y = 125, width = 40, height=40)

def down():
    pendown()
    downButton.destroy()
    upButton = Button(root, text='U/D', bg = "#00F7FF",command=up)
    upButton.place(x = 125, y = 125, width = 40, height=40)

def Blue():
    turtle.pencolor("blue")

def Green():
    turtle.pencolor("green")

def Red():
    turtle.pencolor("red")

def Black():
    turtle.pencolor("black")


forwardButton = Button(root, text='FD', bg = "#00F7FF", command=forward)
forwardButton.place(x = 125, y = 80, width = 40, height=40)

backwardButton = Button(root, text='BK', bg = "#00F7FF",command=backward)
backwardButton.place(x = 125, y = 170, width = 40, height=40)

upButton = Button(root, text='U/D', bg = "#00F7FF",command=up)
upButton.place(x = 125, y = 125, width = 40, height=40)

downButton = Button(root, text='U/D', bg = "#00F7FF",command=down)
downButton.place(x = 125, y = 125, width = 40, height=40)

leftButton = Button(root, text='LT', bg = "#00F7FF",command=left)
leftButton.place(x = 80, y = 125, width = 40, height=40)

rightButton = Button(root, text='RT', bg = "#00F7FF",command=right)
rightButton.place(x = 170, y = 125, width = 40, height=40)

upLeftButton = Button(root, text='ULT', bg = "#00F7FF",command=upLeft)
upLeftButton.place(x = 80, y = 80, width = 40, height=40)

downLeftButton = Button(root, text='DLT', bg = "#00F7FF",command=downLeft)
downLeftButton.place(x = 80, y = 170, width = 40, height=40)

upRightButton = Button(root, text='URT', bg = "#00F7FF",command=upRight)
upRightButton.place(x = 170, y = 80, width = 40, height=40)

downRightButton = Button(root, text='DRT', bg = "#00F7FF",command=downRight)
downRightButton.place(x = 170, y = 170, width = 40, height=40)

clearButton = Button(root, text='CLR', bg = "#00F7FF",command=Clear)
clearButton.place(x = 5, y = 255, width = 40, height=40)

blueButton = Button(root, bg = "blue", command=Blue)
blueButton.place(x = 255, y = 255, height=40, width=40)

redButton = Button(root, bg = "red", command=Red)
redButton.place(x = 210, y = 255, height=40, width=40)

greenButton = Button(root, bg = "green", command=Green)
greenButton.place(x = 165, y = 255, height=40, width=40)

blackButton = Button(root, bg = "black", command=Black)
blackButton.place(x = 120, y = 255, height=40, width=40)

root.geometry("300x300")
root.mainloop()
input()