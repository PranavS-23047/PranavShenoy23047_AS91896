# Module imports
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from game_instructions import GameInstructions

#Window Setup#
root = tk.Tk()
root.title("Guess the Number")
root.geometry("1915x1000")

#Background#
bg_image = Image.open("main_bg.png")

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.image = photo

canvas.bind("<Configure>", resize_image)

resize_image(type("obj", (object,), {"width": 1915, "height": 1000}))

#Button#
button_font = font.Font(family="Times New Roman", size=26)

def open_instructions():
    # Remove title screen
    canvas.pack_forget()
    button1.destroy()

    # Show instructions screen
    instructions = GameInstructions(root)
    instructions.pack(fill="both", expand=True)

button1 = tk.Button(
    root,
    text="CLICK HERE TO BEGIN",
    font=button_font,
    bd=0,
    bg="#feefc8",
    activebackground="#c7b897",
    height=1,
    width=20,
    command=open_instructions
)
button1.place(x=762, y=135)

#Hover Effects#
def on_enter(event):
    button1.config(bg="#c7b897")
def on_leave(event):
    button1.config(bg="#feefc8")

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

#Run Program#
root.mainloop()

