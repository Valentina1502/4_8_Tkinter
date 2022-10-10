#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


if __name__ == '__main__':
    root = Tk()
    c = Canvas(root, width=400, height=400, bg='white')
    c.pack()
    c.create_oval(10, 10, 190, 190,
                  fill='lightgrey',
                  outline='white')
    c.create_arc(10, 10, 190, 190,
                 start=0, extent=45,
                 fill='red')
    c.create_arc(10, 10, 190, 190,
                 start=180, extent=25,
                 fill='orange')
    c.create_arc(10, 10, 190, 190,
                 start=240, extent=100,
                 style=CHORD, fill='green')
    c.create_arc(10, 10, 190, 190,
                 start=160, extent=-70,
                 style=ARC, outline='darkblue',
                 width=5)

    c.create_text(220, 220,
                  text="Hello World,\nPython\nand Tk",
                  justify=CENTER, font="Verdana 14")
    c.create_text(250, 280, text="About this",
                  anchor=SE, fill="grey")

    root.mainloop()
