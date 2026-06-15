import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font

root = tk.Tk()
root.title("Guess the Number")
root.geometry("1915x1000")

bg_image = Image.open("main_bg.png")

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)

    photo = ImageTk.PhotoImage(resized_image)

    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.image = photo

canvas.bind("<Configure>", resize_image)
resize_image(type('obj', (object,), {'width': 700, 'height': 450}))

gtn_frame = tk.Frame(root)
gtn_frame.pack()

button1_font = font.Font(family="Bobby Jones Soft")
button1 = tk.Button(
    root,
    text="CLICK HERE TO BEGIN",
    font=(button1_font, 14),
    padx=0,
    pady=0,
    bd=0,
    bg="#feefc8",
    anchor='center',
    activebackground="#c7b897",
    height=5,
    width=15,
    )
button1.pack(fill=tk.BOTH, expand=True)
button1.place(x=810, y=106.5)
button1.config(height=5, width=25)

root.mainloop()