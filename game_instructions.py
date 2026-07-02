import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
bggi_image = Image.open("gi_bg.png")

class GameInstructions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bggi_image = Image.open("gi_bg.png")
        self.bggi_photo = ImageTk.PhotoImage(self.bggi_image)

        self.bggi_label = tk.Label(self, image=self.bggi_photo)
        self.bggi_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.bggi_label.image = self.bggi_photo

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized_image = bggi_image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.image = photo

canvas.bind("<Configure>", resize_image)

resize_image(type("obj", (object,), {"width": 1915, "height": 1000}))