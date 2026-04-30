import tkinter as tk
root = tk.Tk()

# setting the title of the program

root.title('Guess The Number')

root.geometry("1280x720")
bg = tk.PhotoImage(file="images/mainbg.png")

canvas1= tk.Canvas(root, width=1280, height=720)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0,0, image=bg, anchor="nw")

root.mainloop()