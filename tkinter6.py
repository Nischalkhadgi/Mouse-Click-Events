from tkinter import *

root = Tk()

def leftClick(event):
    print("Left")

def centerClick(event):
    print("Center")

def rightClick(event):
    print("Right")

frame = Frame(root, width = 300, height = 350)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", centerClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()

