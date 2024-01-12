from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#16425d"
MAX_LINE_LENGTH = 35  # Sets the maximum line length



# Create the main window
window = Tk()
window.title("Mik's Speed Typing Test")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget with three rows
text_widget = Text(window, height=4, width=28,
                   wrap='word', font=("Georgia", 20, "bold"),)
text_widget.grid(column=0, row=2, rowspan=4, sticky="nsew")