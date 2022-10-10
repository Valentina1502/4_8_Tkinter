#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def change(event):
    b['fg'] = "red"
    b['activeforeground'] = "red"



if __name__ == '__main__':
    root = Tk()

    b = Button(text='RED', width=10, height=3)
    b.bind('<Button-1>', change)
    b.bind('<Return>', change)
    b.pack()
    root.mainloop()
