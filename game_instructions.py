# Import the modules needed for this screen.
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from game import Game


# Create the instructions screen as a Frame.
class GameInstructions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Load the instructions background image.
        self.bg_image = Image.open("gi_bg.png")

        # Create a label to display the image.
        self.bg_label = tk.Label(self)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Resize the image if the window size changes.
        self.bind("<Configure>", self.resize_background)

        # Create the button font.
        button2_font = font.Font(family="Times New Roman", size=26)

        # Create the button that starts the game.
        self.button = tk.Button(
            self,
            text="→NEXT",
            font=button2_font,
            fg="white",
            bd=0,
            bg="#c4966b",
            activebackground="#b15505",
            height=1,
            width=8,
            command=self.open_game
        )

        # Position the button.
        self.button.place(x=882, y=867)

        # Add hover effects to the button.
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

    # Resize the background image to fit the window.
    def resize_background(self, event):
        if event.widget == self:
            resized_image = self.bg_image.resize(
                (event.width, event.height),
                Image.Resampling.LANCZOS
            )

            self.bg_photo = ImageTk.PhotoImage(resized_image)

            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo

    # Open the game screen.
    def open_game(self):
        # Remove the instructions page.
        self.destroy()

        # Display the game page.
        game = Game(self.master)
        game.pack(fill="both", expand=True)

    # Change button colour when the mouse enters.
    def on_enter(self, event):
        self.button.config(bg="#b15505")

    # Change button colour back when the mouse leaves.
    def on_leave(self, event):
        self.button.config(bg="#c4966b")

