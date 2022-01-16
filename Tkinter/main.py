import tkinter
from tkinter import*
import os

root = Tk()
root.configure(background="#5F5F5F")

drawButton = Button(root, text = "paint")
drawButton.place(x = 220, y = 210, width=60, height=40)

root.geometry("500x500")
root.mainloop()
input()