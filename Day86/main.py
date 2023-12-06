from tkinter import *
from tkinter import filedialog, font, colorchooser, messagebox
import pandas
import random

# Global Variables
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 125
BACKGROUND_COLOR = "#16425D"

# Tkinter
window = Tk()
window.title("Mik's Speed Typing Test")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                highlightthickness=0, bg=BACKGROUND_COLOR)
typewriter = PhotoImage(file="typewriter.png")
# header_text = canvas.create_text(120, 90,
#                                  text="Speed Typing Test", fill="#fff",
#                                  font=("Georgia", 20, "bold"))
typwriter_background = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/4,
                                           image=typewriter)
canvas.grid(row=0, column=0)

# Words
words = pandas.read_csv("common_english_words.csv")
words_list = words['Common Words'].tolist()


frame = Frame(window)

text_area = Text(frame,
                 height=6,
                 width=20,
                 wrap='word',
                 font=("Georgia", 20, "bold"))
words_to_type = [random.choice(words_list) for _ in range(150)]
text_area.insert(INSERT, ' '.join(words_to_type))
# for word in words_to_type:
#     text_area.insert(INSERT, word + "\n")
text_area.tag_configure("matched", foreground="green")
text_area.tag_configure("unmatched", foreground="red")
text_area.grid(column=0, row=1, rowspan=4, sticky="nsew")

text_area.grid(column=0, row=2, rowspan=4, sticky="nsew")

scroll = Scrollbar(frame)

scroll.grid(column=1, row=2, rowspan=4, sticky="ns")
text_area.config(yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)
frame.grid(column=0, row=2, rowspan=4, sticky="nsew")


# Entry
user_entry = Entry(width=30)
user_entry.grid(column=0, row=6, pady=10, ipadx=90, ipady=10)

typed_words = []

def save_entry():
    text = user_entry.get()
    if text:
        typed_words.append(text)
        user_entry.delete(0, END) 

def on_space(event):
    save_entry()



# Bind the Enter key to the save_entry function
user_entry.bind('<space>', on_space)

def highlight_words(self):
    word_to_highlight = user_entry.get()
    text_content = self.text_area.get("1.0", END)  #change


def compare_word():
    user_input = user_entry.get().strip().lower()
    expected_word = words_to_type[0].lower()

    current_line_start = text_area.search(expected_word, "1.0", stopindex="end", exact=True)
    current_line_end = text_area.index(f"{current_line_start}+{len(expected_word)}c lineend")

    text_area.tag_remove("matched", current_line_start, current_line_end)

    if user_input == expected_word:
        text_area.tag_add("matched", current_line_start, current_line_end)
        text_area.tag_config("matched", foreground="green")
        matched_words.append(expected_word)
    else:
        text_area.tag_add("matched", current_line_start, current_line_end)
        text_area.tag_config("matched", foreground="red")
        mistyped_words.append(expected_word)

    words_to_type.pop(0)
    user_entry.delete(0, END)


def countdown(time_sec):
    if time_sec >= 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=f"Time Left: {timeformat}")
        window.after(1000, countdown, time_sec - 1)
    else:
        print("stop")


def reset_labels():
    time_label.config(text="Time Left: 01:00")  # to fix
    CPM_label.config(text=f"Corrected CPM: 0")
    words_per_minute_label.config(text=f"Words Per Minute: 0")
    score_label.config(text=f"Your Best Score: 0")


time_label = Label(text="Time Left: 01:00", font=("Arial", 12), fg="white", bg=BACKGROUND_COLOR)
time_label.grid(column=1, row=1, sticky="E", pady=6)

window.mainloop()