from tkinter import *

root = Tk()
root.geometry("500x500")
root.configure(background="#5F5F5F")

canvas = Canvas()
player = canvas.create_rectangle(230, 230, 80, 80, outline="#fb0", fill="#fb0")
canvas.pack(fill=BOTH, expand=1)

def right():
    player.x += 4

root.bind('<Right>', lambda event: right)

root.mainloop()
input()