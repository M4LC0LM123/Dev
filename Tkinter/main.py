
from tkinter import*
from turtle import*

def square():
    for i in range(4):
        fd(100)
        lt(90)

def triangle():
    for i in range(4):
        fd(100)
        lt(120)

def cum():
    lt(90)
    fd(100)
    rt(90)

def Triangle():
    fd(100)
    rt(120)
    fd(100)
    rt(120)
    fd(150)

window1 = Tk()
button = Button(window1,text='Square', command=square)
button.place(x=75,y=50,width=60)
button2 = Button(window1,text='Triangle', command=triangle)
button2.place(x=75,y=80,width=60)
button3 = Button(window1,text='CUM', command=cum)
button3.place(x=75,y=120,width=60)
input()