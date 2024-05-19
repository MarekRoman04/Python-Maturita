### STDLIB
import math
import random
import tkinter as tk

WIDTH = 800
HEIGHT = 600

c = tk.Canvas(width=WIDTH, height=HEIGHT)
c.pack()


def polygon(pos, n, a) -> None:
    x = pos[0]
    y = pos[1]
    angle = 360 / n
    for i in range(n):
        c.create_line(
            x + a * math.sin(math.radians(angle * i)),
            y + a * math.cos(math.radians(angle * i)),
            x + a * math.sin(math.radians(angle * (i + 1))),
            y + a * math.cos(math.radians(angle * (i + 1))),
        )


def triangle_polygon(pos, n, a) -> None:
    x = pos[0]
    y = pos[1]
    angle = 360 / n
    for i in range(n):
        c.create_polygon(
            x,
            y,
            x + a * math.sin(math.radians(angle * i)),
            y + a * math.cos(math.radians(angle * i)),
            x + a * math.sin(math.radians(angle * (i + 1))),
            y + a * math.cos(math.radians(angle * (i + 1))),
            fill=f"#{random.randrange(256**3):06x}",
        )


def chess_board(pos, size, a) -> None:
    color = "white"
    y = pos[1]
    for _ in range(size[1]):
        color = "white" if color == "black" else "black"
        x = pos[0]
        for _ in range(size[0]):
            color = "white" if color == "black" else "black"
            c.create_rectangle(x, y, x + a, y + a, fill=color)
            x += a
        y += a
