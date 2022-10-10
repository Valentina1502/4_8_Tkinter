#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def event_info(event):
    print(type(event))
    print(event)
    print(event.time)
    print(event.x_root)
    print(event.y_root)


if __name__ == '__main__':
    root = Tk()
    root.bind('a', event_info)
    root.mainloop()
