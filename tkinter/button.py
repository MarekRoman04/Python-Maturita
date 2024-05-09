# STDLIB
import tkinter as tk
from typing import Callable

def create_button(canvas: tk.Canvas, coords: tuple[float, float, float, float], on_click: Callable, name: str | None) -> int:
    ...

def clear_button(canvas: tk.Canvas, coords: tuple[float, float, float, float], name: str | None) -> int:
    return create_button(canvas, coords, lambda: canvas.delete("all"), name)