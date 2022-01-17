import tkinter
import tkinter as tk 
from tkinter import *
import os

root = Tk()
root.configure(background="#5F5F5F")

def openPaint():
    os.system(r'c:\Users\lukaa\Documents\GitHub\Tkinter\Scripts\drawStuff.py')

drawButton = Button(root, text = "paint", command = openPaint)
drawButton.place(x = 220, y = 210, width=60, height=40)

root.geometry("500x500")
root.mainloop()
input()