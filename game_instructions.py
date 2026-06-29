import tkinter as tk

class GameInstructions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#feefc8")

        # Title
        title = tk.Label(
            self,
            text="GAME INSTRUCTIONS",
            font=("Times New Roman", 28, "bold"),
            bg="#feefc8"
        )
        title.pack(pady=30)