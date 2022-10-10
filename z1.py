#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def add():
    product = []
    select = list(box.curselection())
    select.reverse()
    for item in select:
        ad = box.get(item)
        product.append(ad)
    for val in product:
        box2.insert(0, val)
    for n in select:
        box.delete(n)


def back():
    product = []
    select = list(box2.curselection())
    select.reverse()
    for item in select:
        ad = box2.get(item)
        product.append(ad)
    for val in product:
        box.insert(0, val)
    for n in select:
        box2.delete(n)


if __name__ == '__main__':
    root = Tk()
    root.title('Покупки')
    root.geometry('310x240')

    products = [
        'apple',
        'bananas',
        'carrot',
        'bread',
        'butter',
        'meat',
        'potato'
    ]

    box = Listbox(selectmode=EXTENDED)
    box.pack(side=LEFT)
    box2 = Listbox(selectmode=EXTENDED)
    box2.pack(side=RIGHT)

    f = Frame()
    f.pack(side=LEFT, padx=10)
    Button(f, text="--->>", command=add).pack(fill=X)
    Button(f, text="<<---", command=back).pack(fill=X)

    for i in products:
        box.insert(END, i)
    root.mainloop()
