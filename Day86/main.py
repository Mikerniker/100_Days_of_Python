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
typwriter_background = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/4,
                                           image=typewriter)
canvas.grid(row=0, column=0)

# Words
words = pandas.read_csv("common_english_words.csv")
words_list = words['Common Words'].tolist()


frame = Frame(window)

text_area = Text(frame,
                 height=6,
                 width=25,
                 wrap='word',
                 font=("Georgia", 20, "bold"))
words_to_type = [random.choice(words_list) for _ in range(150)]
for word in words_to_type:
    text_area.insert(INSERT, word + " ")
text_area.tag_configure("matched", foreground="green")
text_area.tag_configure("unmatched", foreground="red")
text_area.grid(column=0, row=2, rowspan=4, sticky="nsew")


scroll = Scrollbar(frame)

scroll.grid(column=1, row=2, rowspan=4, sticky="ns")
text_area.config(yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)
frame.grid(column=0, row=2, rowspan=4, sticky="nsew")


def select_first_word():
    # Find the position of the first space after the starting index
    start = "1.0"
    first_space_index = text_area.search(" ", start, stopindex=END, regexp=True)

    if first_space_index:
        # Select the word from the starting index to the first space
        text_area.tag_add("SEL", start, first_space_index)

        # Get the word to be returned
        selected_word = text_area.get(start, first_space_index)

        # return selected_word, "1.0", first_space_index
        return selected_word, start, first_space_index

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


def compare_word(event):
    global current_word_index

    user_input = user_entry.get().strip().lower()

    start = "1.0"
    expected_word = words_to_type[current_word_index]
    end = text_area.search(expected_word, start, stopindex="end")

    unmatched_tag = None 
    if end:
        end = f"{end}+{len(expected_word)}c"

        word = text_area.get(start, end).strip().lower()

        # Check existing tags of the word
        existing_tags = text_area.tag_names(start)
        if "matched" in existing_tags or "unmatched" in existing_tags:
            # Preserve the existing color
            color = existing_tags[0].split("-")[0]
        else:
            # Use default color if no existing tags
            color = "black"

        if user_input == expected_word:
            # Apply "matched" tag to the correct word
            tag_name = f"{color}-matched"
            text_area.tag_add(tag_name, start, end)
            text_area.tag_config(tag_name, foreground="green")
            matched_words.append((expected_word, color))
        else:
            tag_name = f"{color}-unmatched"
            text_area.tag_add(tag_name, start, end)
            text_area.tag_config(tag_name, foreground="red")

            unmatched_words.append((expected_word, color))

    # Move to the next word in the list
    current_word_index += 1

    if current_word_index >= len(words_to_type):
        current_word_index = 0  # Start over if all words are typed

    # Clear the user's input
    user_entry.delete(0, END)



def countdown(time_sec):
    matched = 0
    if time_sec >= 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=f"Time Left: {timeformat}")
        window.after(1000, countdown, time_sec - 1)
    else:
        for word in matched_words:
            matched += len(word)

        word_per_min = matched / 5
        print(f"User type words: {len(user_words)} "
                  f"CPM {matched} words per minute: {word_per_min}")
        return matched, word_per_min



def reset_labels():
    time_label.config(text="Time Left: 01:00")  # to fix
    CPM_label.config(text=f"Corrected CPM: 0")
    words_per_minute_label.config(text=f"Words Per Minute: 0")
    score_label.config(text=f"Your Best Score: 0")


time_label = Label(text="Time Left: 01:00", font=("Arial", 12), fg="white", bg=BACKGROUND_COLOR)
time_label.grid(column=1, row=1, sticky="E", pady=6)

window.mainloop()

# RAW CPM
all_chars = 0
for word in user_words:
    all_chars += len(word)
