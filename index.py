# Import the modules needed for the program.
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from game_instructions import GameInstructions

# Create the main window.
root = tk.Tk()
root.title("Guess the Number!")
root.geometry("1915x1000")

# Load the background image for the main menu.
bg_image = Image.open("main_bg.png")

# Create a canvas to display the background image.
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)


# Resize the background image whenever the window size changes.
def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    # Remove the old image and display the resized one.
    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor="nw")

    # Store a reference so the image stays visible.
    canvas.image = photo


# Run the resize function whenever the window changes size.
canvas.bind("<Configure>", resize_image)

# Display the background when the program starts.
resize_image(type("obj", (object,), {"width": 1915, "height": 1000}))

# Create the font used for the button.
button1_font = font.Font(family="Times New Roman", size=26)


# Open the instructions screen when the button is clicked.
def open_instructions():
    # Hide the main menu.
    canvas.pack_forget()
    button1.destroy()

    # Display the instructions screen.
    instructions = GameInstructions(root)
    instructions.pack(fill="both", expand=True)


# Create the button.
button1 = tk.Button(
    root,
    text="CLICK HERE TO BEGIN",
    font=button1_font,
    bd=0,
    bg="#feefc8",
    activebackground="#c7b897",
    height=1,
    width=20,
    command=open_instructions
)

# Position the button.
button1.place(x=762, y=135)


# Change the button colour when the mouse is over it.
def on_enter(event):
    button1.config(bg="#c7b897")

# Change the button back when the mouse leaves.
def on_leave(event):
    button1.config(bg="#feefc8")

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

# Keep the program running until the user closes it.
root.mainloop()