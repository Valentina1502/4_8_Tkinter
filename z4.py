#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas, ARC


if __name__ == '__main__':

    root = Tk()
    root.title('Рисунок')
    root.geometry('500x400')

    c = Canvas(root, width=500, height=400, bg='white')
    c.pack()

    # Создаем основу дома и солнце
    circle = c.create_oval(383, 18, 450, 84, fill="#FFFF00")
    rectangle = c.create_rectangle(129, 143, 340, 360, fill='orange')
    triangle = c.create_polygon(232, 30, 90, 144, 375, 143, fill='#804040')

    # Создаем собаку
    triangle2 = c.create_polygon(3, 238, 45, 197, 45, 226,
                                 77, 226, 76, 197, 118, 237,
                                 83, 215, 83, 289, 40, 289,
                                 40, 214, fill='#804040')
    triangle3 = c.create_polygon(28, 305, 28, 332, 17, 332,
                                 17, 345, 42, 345, 42, 306, fill="#400d00")
    triangle4 = c.create_polygon(80, 305, 94, 305, 95, 332,
                                 105, 332, 105, 345, 80, 345, fill="#400d00")
    rectangle2 = c.create_rectangle(42, 289, 80, 345, fill='#804040')
    rectangle3 = c.create_rectangle(54, 290, 67, 309, fill='red')
    rectangle4 = c.create_rectangle(38, 339, 60, 352, fill='#804040')
    rectangle5 = c.create_rectangle(61, 339, 84, 352, fill='#804040')
    line1 = c.create_line(20, 338, 20, 344)
    line2 = c.create_line(25, 338, 25, 344)
    line3 = c.create_line(41, 347, 41, 353)
    line4 = c.create_line(45, 345, 45, 353)
    line5 = c.create_line(76, 345, 76, 353)
    line6 = c.create_line(79, 347, 79, 353)
    line7 = c.create_line(97, 338, 97, 345)
    line8 = c.create_line(101, 338, 101, 345)
    line9 = c.create_line(61, 289, 61, 300)
    circle2 = c.create_oval(50, 260, 72, 274, fill="#400000")
    circle5 = c.create_oval(31, 237, 53, 259, fill="white")
    circle6 = c.create_oval(45, 247, 49, 251, fill="black")
    circle7 = c.create_oval(66, 237, 88, 259, fill="white")
    circle8 = c.create_oval(73, 247, 77, 251, fill="black")

    # Детали к дому
    rectangle7 = c.create_rectangle(200, 160, 265, 227, fill='white')
    line10 = c.create_line(232, 160, 232, 227)
    line11 = c.create_line(200, 195, 265, 195)

    # Создаем цикл, для вывода травы
    x = 0
    while x < 500:
        c.create_arc(x, 455, x+40, 350, start=180, extent=-80, style=ARC, width=3, outline='green')
        x += 11

    root.mainloop()
    