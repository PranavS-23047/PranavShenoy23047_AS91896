# Import the modules needed for the game screen.
import tkinter as tk
from PIL import Image, ImageTk


# Create the game screen as a Frame.
class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Load the game background image.
        self.bg_image = Image.open("game_bg.png")

        # Create a label to display the image.
        self.bg_label = tk.Label(self)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Resize the background when the window changes size.
        self.bind("<Configure>", self.resize_background)

    # Resize the image so it always fills the window.
    def resize_background(self, event):
        if event.widget == self:
            resized_image = self.bg_image.resize(
                (event.width, event.height),
                Image.Resampling.LANCZOS
            )

            self.bg_photo = ImageTk.PhotoImage(resized_image)

            self.bg_label.config(image=self.bg_photo)

            # Store the image to stop it being removed from memory.
            self.bg_label.image = self.bg_photo