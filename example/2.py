#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def add():
    box.insert(END, entry.get())


def delete():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box.delete(i)


def save():
    f = open('list000.txt', 'w')
    f.writelines("\n".join(box.get(0, END)))
    f.close()


if __name__ == '__main__':
    root = Tk()

    box = Listbox(selectmode=EXTENDED)
    box.pack(side=LEFT)
    scroll = Scrollbar(command=box.yview)
    scroll.pack(side=LEFT, fill=Y)
    box.config(yscrollcommand=scroll.set)

    f = Frame()
    f.pack(side=LEFT, padx=10)
    entry = Entry(f)
    entry.pack(anchor=N)
    Button(f, text="Add", command=add).pack(fill=X)
    Button(f, text="Delete", command=delete).pack(fill=X)
    Button(f, text="Save", command=save).pack(fill=X)
    root.mainloop()
