from tkinter import *
import time

BACKGROUND_COLOR = "#003C43"
MAX_LINE_LENGTH = 35 


instructions = "Don't stop writing or your text will disappear!"
countdown_time = 10


def countdown():
    time_elapse = int(check_elapsed_time())
    if time_elapse > 5:
        remaining_time = countdown_time - time_elapse
        if remaining_time >= 0:
            time_label.config(text=f"Time Left: {remaining_time:02d}")
        else:
            time_label.config(text="Time Left: 00")
            text_widget.delete('1.0', END)
    else:
        time_label.config(text=f"Time Left: {5:02d}")
    window.after(1000, countdown)

def on_key_release(event):
    """ Record the time when a key is released and starts the timer if it's not already running"""
    global last_key_release_time, timer_running
    last_key_release_time = time.time()
    if not timer_running:
        timer_running = True


def on_key_press(event):
    """Stops the timer when a key is pressed"""
    global timer_running
    timer_running = False
    if len(text_widget.get("1.0", "end-1c")) > 0:
        countdown()


def check_elapsed_time():
    global last_key_release_time
    # Calculate the elapsed time since the last key release
    elapsed_time = time.time() - last_key_release_time

    return elapsed_time


# Create the main window
window = Tk()
window.title("Mik's Disappearing Text")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget
text_widget = Text(window, height=10, width=40,
                   wrap='word', font=("Georgia", 25),
                   bg=BACKGROUND_COLOR, bd=0, fg="#FFF2D7", insertbackground="#FFF2D7")
text_widget.grid(column=0, row=3, rowspan=4, sticky="nsew")
# Bind the text widget to the event for key release
text_widget.bind("<KeyRelease>", on_key_release)
text_widget.bind("<KeyPress>", on_key_press)



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
