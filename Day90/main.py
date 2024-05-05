from tkinter import *
import time

BACKGROUND_COLOR = "#135D66"


# Create the main window
window = Tk()
window.title("Mik's Disappearing Text")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget with three rows
text_widget = Text(window, height=10, width=40,
                   wrap='word', font=("Georgia", 25))
text_widget.grid(column=0, row=3, rowspan=4, sticky="nsew")

window.mainloop()
