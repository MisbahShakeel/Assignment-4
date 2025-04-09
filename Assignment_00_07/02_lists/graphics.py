import tkinter as tk
import time

class Canvas:
    def __init__(self, width, height):
        self._tk = tk.Tk()
        self._tk.title("Canvas")
        self._canvas = tk.Canvas(self._tk, width=width, height=height)
        self._canvas.pack()
        self._mouse_x = 0
        self._mouse_y = 0
        self._click = None
        self._canvas.bind("<Motion>", self._on_mouse_move)
        self._canvas.bind("<Button-1>", self._on_mouse_click)
        self._objects = {}
        self._next_id = 1
        self._tk.update()

    def _on_mouse_move(self, event):
        self._mouse_x = event.x
        self._mouse_y = event.y

    def _on_mouse_click(self, event):
        self._click = (event.x, event.y)

    def get_mouse_x(self):
        return self._mouse_x

    def get_mouse_y(self):
        return self._mouse_y

    def get_last_click(self):
        while self._click is None:
            self._tk.update()
            time.sleep(0.05)
        x, y = self._click
        self._click = None
        return x, y

    def wait_for_click(self):
        while self._click is None:
            self._tk.update()
            time.sleep(0.05)

    def create_rectangle(self, x1, y1, x2, y2, color):
        obj_id = self._next_id
        self._next_id += 1
        rect = self._canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        self._objects[obj_id] = rect
        return obj_id

    def moveto(self, obj_id, x, y):
        obj = self._objects[obj_id]
        bbox = self._canvas.bbox(obj)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        self._canvas.coords(obj, x, y, x + width, y + height)

    def set_color(self, obj_id, color):
        obj = self._objects[obj_id]
        self._canvas.itemconfig(obj, fill=color)

    def find_overlapping(self, x1, y1, x2, y2):
        overlap = self._canvas.find_overlapping(x1, y1, x2, y2)
        result = []
        for obj_id, tk_id in self._objects.items():
            if tk_id in overlap:
                result.append(obj_id)
        return result

    def close(self):
        self._tk.quit()
        self._tk.destroy()
