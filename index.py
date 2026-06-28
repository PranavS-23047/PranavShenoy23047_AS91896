# module imports
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font

# window setup
root = tk.Tk()
root.title("Guess the Number")
root.geometry("1915x1000")

# canvas and image backgrounds
bg_image = Image.open("main_bg.png")
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# image resizing
def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.image = photo

# frames and canvas
canvas.bind("<Configure>", resize_image)
resize_image(type('obj', (object,), {'width': 700, 'height': 450}))
gtn_frame = tk.Frame(root)
gtn_frame.pack()

# button design and setup
button1_font = font.Font(family="Times New Roman", size=26)
button1 = tk.Button(
    root,
    text="CLICK HERE TO BEGIN",
    font=button1_font,
    bd=0,
    bg="#feefc8",
    anchor='center',
    activebackground="#c7b897",
    height=1,
    width=20,
    )
button1.place(x=762, y=135)

#effects for buttons - aesthetic purposes
def on_enter(event):
    button1.config(bg="#c7b897", fg="black")
def on_leave(event):
    button1.config(bg="#feefc8", fg="black")

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

#starts event loop and keeps window responsive until window is closed by user
root.mainloop()
