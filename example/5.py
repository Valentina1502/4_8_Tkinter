#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def font1(font):
    l['font'] = font


if __name__ == '__main__':
    root = Tk()
    l = Label(text='Hello world')
    l.pack()
    Button(command=
           lambda f='Veranda': font1(f)).pack()
    Button(command=
           lambda f='Times': font1(f)).pack()
    root.mainloop()
