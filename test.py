from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("GUESS THE NUMBER")

win.geometry("1915x1000")

original_image = Image.open("main_bg.png")

canvas = Canvas(win)
canvas.pack(fill=BOTH, expand=True)

def resize_image(event):

    new_width = event.width
    new_height = event.height

    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    photo = ImageTk.PhotoImage(resized_image)

    canvas.delete("all")
    canvas.create_image(0, 0, image=photo, anchor='nw')

    canvas.image = photo

resize_image(type('obj', (object,), {'width': 700, 'height': 450}))

canvas.bind("<Configure>", resize_image)

image_label = tk.Label(gtn_frame, image=background_image_tk)
image_label.image = background_image_tk
image_label.place(x=0, y=0, relwidth=1, relheight=1)

button_canvas = tk.Canvas(gtn_frame, width=400, height=60)
button_canvas.place(x=753, y=107)

button1 = tk.Button(button_canvas, text="CLICK HERE TO BEGIN", borderwidth=0, highlightthickness=0)
button_canvas.create_window(0, 0, anchor="nw", window=button1)
button1.config(bg="#feefc8")
button1.config(font=("Bobby Jones Soft", 26))

def on_enter(event):
    button1.config(bg="#008a48")

def on_leave(event):
    button1.config(bg="#00bf63")

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

win.mainloop()