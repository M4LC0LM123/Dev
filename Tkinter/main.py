from tkinter import*
from turtle import*

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

forwardButton = Button(root, text='FD', bg = "#00F7FF", command=forward)
forwardButton.place(x = 75, y = 25, width = 40, height=40)

backwardButton = Button(root, text='BK', bg = "#00F7FF",command=backward)
backwardButton.place(x = 75, y = 115, width = 40, height=40)

upButton = Button(root, text='UP', bg = "#00F7FF",command=up)
upButton.place(x = 75, y = 70, width = 40, height=40)

leftButton = Button(root, text='LT', bg = "#00F7FF",command=left)
leftButton.place(x = 29, y = 70, width = 40, height=40)

rightButton = Button(root, text='RT', bg = "#00F7FF",command=right)
rightButton.place(x = 119, y = 70, width = 40, height=40)

input()