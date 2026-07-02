import tkinter as tk
from PIL import Image, ImageTk

class GameInstructions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bg_image = Image.open("gi_bg.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg_label.image = self.bg_photo
