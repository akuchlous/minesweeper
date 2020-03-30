#!/usr/bin/env python3

import tkinter as tk
from functools import partial
import pdb

def change(x,y):
    bname = allButtons[(i,j)]
    bname.configure(text = "clicked: %d, %d" %(i,j))

window = tk.Tk()
allButtons = {}

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=5
        )
        frame.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
        button = tk.Button(master=frame, text=f"Row {i}\nColumn {j}", padx=5, pady=5, command=partial(change, i,j))
        button.pack()
        allButtons[(i,j)] = button
	
print(allButtons)
window.mainloop()
