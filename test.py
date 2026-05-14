from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Frame
from index import gtn_frame

win = Tk()
win.title("Guess the Number")

win.geometry("1915x1000")

original_image = Image.open("main_bg.png")

canvas = Canvas(win)
canvas.pack(fill=BOTH, expand=True)


def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    photo = ImageTk.PhotoImage(resized_image)

    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor='nw')

    canvas.image = photo

resize_image(type('obj', (object,), {'width': 700, 'height': 450}))

canvas.bind("<Configure>", resize_image)

win.mainloop()