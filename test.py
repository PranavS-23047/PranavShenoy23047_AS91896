from tkinter import (Tk, Canvas, Button, Frame)
from PIL import ImageTk, Image
from PIL._tkinter_finder import tk

from index import root

root = tk.Tk()
root.title("Guess the Number")
root.geometry("1915x1000")

original_image = Image.open("main_bg.png")

canvas = Canvas(root)
canvas.pack(fill="both", expand=True)

def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    photo = ImageTk.PhotoImage(resized_image)

    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.image = photo

canvas.bind("<Configure>", resize_image)
resize_image(type('obj', (object,), {'width': 700, 'height': 450}))

gtn_frame = Frame(root)
gtn_frame.pack()

root.geometry("400x60")

# The button will now grow/shrink as you resize the window
button1 = tk.Button(root, text="CLICK HERE TO BEGIN")
button1.pack(fill=tk.BOTH, expand=True)
button1.place(x=50, y=90)

root.mainloop()