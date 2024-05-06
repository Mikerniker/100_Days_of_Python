from tkinter import *
import time

BACKGROUND_COLOR = "#135D66"


# Create the main window
window = Tk()
window.title("Mik's Disappearing Text")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget
text_widget = Text(window, height=10, width=40,
                   wrap='word', font=("Georgia", 25))
text_widget.grid(column=0, row=3, rowspan=4, sticky="nsew")


# Labels
header_label = Label(text="Disappearing Text",
                     font=("Georgia", 30, "bold"), fg="white",
                     bg=BACKGROUND_COLOR)
header_label.grid(column=0, row=1, pady=5)

instructions_label = Label(text=instructions, font=("Arial", 11),
                           wraplength=text_widget.winfo_reqwidth(),
                           justify="center", fg="white", bg=BACKGROUND_COLOR)
instructions_label.grid(column=0, row=2, pady=5)


window.mainloop()
