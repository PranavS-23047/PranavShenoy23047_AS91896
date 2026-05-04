import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Frame, Label, BOTH

root = tk.Tk()
root.title('Guess The Number')
root.geometry("1915x1000")

background_image = Image.open('images/mainbg.png')
background_image = background_image.resize((1920, 1080), Image.Resampling.LANCZOS)
background_image_tk = ImageTk.PhotoImage(background_image)

gtn_frame = Frame(root)
gtn_frame.pack(fill=BOTH, expand=True)

image_label = Label(gtn_frame, image=background_image_tk)
image_label.image = background_image_tk
image_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()