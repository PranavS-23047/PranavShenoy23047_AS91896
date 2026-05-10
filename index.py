import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Guess The Number')
root.geometry("1915x1000")

background_image = Image.open('images/mainbg.png')
background_image = background_image.resize((1920, 1080), Image.Resampling.LANCZOS)
background_image_tk = ImageTk.PhotoImage(background_image)

gtn_frame = tk.Frame(root)
gtn_frame.pack(fill=tk.BOTH, expand=True)

image_label = tk.Label(gtn_frame, image=background_image_tk)
image_label.image = background_image_tk
image_label.place(x=0, y=0, relwidth=1, relheight=1)


button_canvas = tk.Canvas(gtn_frame, width=400, height=60)
button_canvas.place(x=753, y=107)

button1 = tk.Button(button_canvas, text="CLICK HERE TO BEGIN", borderwidth=0, highlightthickness=0)
button_canvas.create_window(0, 0, anchor="nw", window=button1)
button1.config(bg="#feefc8")
button1.config(font=("Bobby Jones Soft", 26))

root.mainloop()