import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font

from index import canvas

root=tk.Tk()
root.title("Instructions")

class GameInstructions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Load the background image
        self.bg_image = Image.open("gi_bg.png")

        # Create a label to hold the background
        self.bg_label = tk.Label(self)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Resize the image whenever the frame changes size
        self.bind("<Configure>", self.resize_background)

    def resize_background(self, event):
        # Only resize if the Frame itself is resizing, not its child widgets
        if event.widget == self:
            # Resize image to fit the window
            resized_image = self.bg_image.resize((event.width, event.height), Image.Resampling.LANCZOS)

            # Convert to a Tkinter image
            self.bg_photo = ImageTk.PhotoImage(resized_image)

            # Display the image
            self.bg_label.config(image=self.bg_photo)
            # Keep a reference to prevent garbage collection
            self.bg_label.image = self.bg_photo

#Button
button2_font = font.Font(family="Times New Roman", size=26)

def open_instructions():
    # Remove title screen
    canvas.pack_forget()
    button2.destroy()

    # Show instructions screen
    instructions = GameInstructions(root)
    instructions.pack(fill="both", expand=True)

button2 = tk.Button(
    root,
    text="CLICK HERE TO BEGIN",
    font=button2_font,
    bd=0,
    bg="#feefc8",
    activebackground="#c7b897",
    height=1,
    width=20,
    command=open_instructions
)
button2.place(x=762, y=135)

#Hover Effects
def on_enter(event):
    button2.config(bg="#c7b897")
def on_leave(event):
    button2.config(bg="#feefc8")

button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)