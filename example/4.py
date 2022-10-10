#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


class RedButton:
    def __init__(self):
        self.b = Button(text='RED', width=10, height=3)
        self.b.bind('<Button-1>', self.change)
        self.b.pack()

    def change(self, event):
        self.b['fg'] = "red"
        self.b['activeforeground'] = "green"


if __name__ == '__main__':
    root = Tk()
    RedButton()

    root.mainloop()
