#!/usr/bin/env python3
import pdb
import random
from tkinter import *
from functools import partial
from itertools import product
import time

# produce the set of coordinates of the buttons
positions = product(range(10), range(10))
pressed = [[0 for x in range(10)] for y in range(10)]
button_ids =   [[0 for x in range(10)] for y in range(10)]
gamePos = [[0 for x in range(10)] for y in range(10)]
gameOver=0


def numN(x,y, gamePos):
    c=0
    for n,m in [(-1,-1), (-1,0),(-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        if (0 <= x+n and x+n<len(gamePos)):    # check row
            if (0 <= y+m and y+m<len(gamePos[0])):  # check col
                c+=gamePos[x+n][y+m]
    return c

def change(x,y):
    global gameOver
    if (gameOver) : return 
    if (pressed[x][y]): return 
    pressed[x][y] = 1
    # get the button's identity, destroy it
    button = button_ids[x][y]
    button.configure(bg="blue")
    if (gamePos[x][y] == 1):  
        button.config(text="B", bg="red")
        gameOver=1
    else: 
        button.config(text=str(numN(x,y, gamePos)))

win = Tk()
frame = Frame(win)
frame.pack()

for i in range(10):
    # shape the grid
    setsize = Canvas(frame, width=30, height=0).grid(row=11, column=i)
    setsize = Canvas(frame, width=0, height=30).grid(row=i, column=11)

numberList = [0,0,0,0,0,0,0,0,0,0,1]

for x,y in positions:
    val = random.choice(numberList)
    if (0):
        button = Button(frame, command=partial(change, x,y), text=str(val))
    else:
        button = Button(frame, command=partial(change, x,y))
    button.grid(row=x, column=y, sticky="n,e,s,w")
    button_ids[x][y] = button
    gamePos[x][y] = val

win.minsize(width=270, height=270)
win.title("Too many squares")
win.mainloop()
