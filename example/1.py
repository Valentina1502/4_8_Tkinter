#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


if __name__ == '__main__':
    root = Tk()
    lbox = Listbox(width=15, height=8)
    lbox.pack()

    for i in ('0ne', 'two', 'tree', 'four', 'five', 'six', 'seven'):
        lbox.insert(0, i)
    root.mainloop()
