#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def in_focus(event):
    c.itemconfig(rect, fill='green', width=2)


if __name__ == '__main__':
    root = Tk()
    c = Canvas(width=200, height=200,
               bg='white')
    c.pack()
    rect = c.create_rectangle(
        80, 80, 120, 120, fill='lightgreen')

    c.coords(rect, 70, 70, 130, 130)
    c.bind('<FocusIn>', in_focus)

    root.mainloop()
