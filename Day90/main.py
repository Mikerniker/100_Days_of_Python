from tkinter import *
import time

BACKGROUND_COLOR = "#003C43"
MAX_LINE_LENGTH = 35 


instructions = "Don't stop writing or your text will disappear!"
countdown_time = 10



def on_key_release(event):
    global last_key_release_time, timer_running
    # Record the time when a key is released
    last_key_release_time = time.time()
    # Start the timer only if it's not already running
    if not timer_running:
        timer_running = True


# Create the main window
window = Tk()
window.title("Mik's Disappearing Text")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget
text_widget = Text(window, height=10, width=40,
                   wrap='word', font=("Georgia", 25),
                   bg=BACKGROUND_COLOR, bd=0, fg="#FFF2D7", insertbackground="#FFF2D7")
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

time_label = Label(text="Time Left: 06", font=("Arial", 12), fg="white",
                   bg=BACKGROUND_COLOR)
time_label.grid(column=0, row=7, pady=6)


window.mainloop()
