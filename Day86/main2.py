from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#16425d"
MAX_LINE_LENGTH = 35  # Sets the maximum line length


def insert_words():
    # Words
    global current_line
    words = pandas.read_csv("common_english_words.csv")
    words_list = words['Common Words'].tolist()
    words_to_type = [random.choice(words_list) for _ in range(150)]
    print(words_to_type)

    for word in words_to_type:
        text_widget.insert("1.0", word + " ")

        text_widget.tag_configure("center", justify="center")
        text_widget.tag_add("center", "1.0", "end")



current_word_index = 0
current_line_index = 0
user_words = []

def update_word_colors():
    # Iterate through each word and compare with user input
    for i, expected_word in enumerate(expected_words):
        # start = f"1.{len(' '.join(expected_words[:i])) + 1}"
        # end = f"1.{len(' '.join(expected_words[:i + 1]))}"

        start = f"{current_line_index + 1}.{len(' '.join(expected_words[:i])) + 1}"
        end = f"{current_line_index + 1}.{len(' '.join(expected_words[:i + 1]))}"

        if i < len(user_words) and user_words[i] == expected_word.lower():
            print("match")
            text_widget.tag_configure(f"match_{i}", foreground="green")
            text_widget.tag_add(f"match_{i}", start, end)
        elif i < len(user_words) and user_words[i] != expected_word.lower():
            print("no match")
            text_widget.tag_configure(f"no_match_{i}", foreground="red")
            text_widget.tag_add(f"no_match_{i}", start, end)
# Create the main window
window = Tk()
window.title("Mik's Speed Typing Test")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget with three rows
text_widget = Text(window, height=4, width=28,
                   wrap='word', font=("Georgia", 20, "bold"),)
text_widget.grid(column=0, row=2, rowspan=4, sticky="nsew")


# Run the Tkinter event loop
window.mainloop()