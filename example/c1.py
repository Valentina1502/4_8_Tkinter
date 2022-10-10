#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


if __name__ == '__main__':
    root = Tk()
    c = Canvas(root, width=400, height=400, bg='white')
    c.pack()
    c.create_line(20, 15, 170, 50)
    c.create_line(20, 80, 100, 60, fill='green',
                  width=5, arrow=LAST, dash=(10, 2),
                  activefill='lightgreen',
                  arrowshape="10 20 10")
    c.create_rectangle(10, 10, 190, 60)
    c.create_rectangle(200, 80, 240, 160,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4))
    c.create_polygon(200, 200, 120, 250, 280, 290)
    c.create_polygon(40, 110, 160, 110,
                     190, 180, 10, 180,
                     fill='orange', outline='black')
    c.create_oval(300, 100, 320, 120, width=2)
    c.create_oval(250, 10, 270, 70,
                  fill='grey70', outline='white')
    root.mainloop()
