import random
import time
from tkinter import *

def change(events):
    if circle == True:
        fiewCircle()
    else:
        fiewColors()
def fiewColors():
    global first
    if first == False:
        return
    first = False

    while True:
        color = random.choice(colors)
        x = random.randint(0, 599)
        y = random.randint(0, 599)
        c.create_rectangle(x, y, x + 2, y + 2, fill=color, width=0)
        if circle:
            break
        c.update_idletasks()
        c.update()
    fiewCircle()

def fiewCircle():
    global first
    if first == False:
        return
    first = False
    while True:
        x = random.randint(0, 599)
        y = random.randint(0, 599)
        r = random.randint(1, 50)
        c.create_oval(x,y,x+r, y+r, fill=random.choice(colors))
        c.update_idletasks()
        c.update()
        time.sleep(0.003)
        if not circle:
            break
    fiewColors()

def again():
    global first, circle
    circle = not circle
    first = True
    c.delete("all")
first = True
circle = False
w = Tk()
c = Canvas(width=600, height=600)
c.pack()
b = Button(c, text='again', font=(None, 24), bg = '#fff', command=again)
b.place(x = 0, y = 250)
colors = ['red', 'purple', 'cyan', 'tomato', 'silver', 'gold', 'green', 'springgreen', 'yellow', 'indigo']
c.bind('<Enter>', change)

w.mainloop()