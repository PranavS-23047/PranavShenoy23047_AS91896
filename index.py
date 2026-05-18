from tkinter import Tk, Canvas, Button
from PIL import ImageTk, Image


win = Tk()
win.title("Guess the Number")
win.geometry("1915x1000")


original_image = Image.open("main_bg.png")


canvas = Canvas(win, highlightthickness=0)
canvas.pack(fill="both", expand=True)


btn = Button(
    win,
    text="CLICK HERE TO BEGIN",
    font=("Bobby Jones Soft", 20),
    bg="#feefc8",
)

btn.place(x=400, y=60)

def resize_image(event):
    global bg_photo


    new_width = event.width
    new_height = event.height


    resized_image = original_image.resize(
        (new_width, new_height),
        Image.LANCZOS
    )


    bg_photo = ImageTk.PhotoImage(resized_image)


    canvas.delete("all")


    canvas.create_image(
        0,
        0,
        image=bg_photo,
        anchor="nw"
    )

    canvas.create_window(
        new_width // 2,
        new_height // 2,
        window=btn,
        width=new_width // 6,
        height=new_height // 12
    )

canvas.bind("<Configure>", resize_image)

win.mainloop()