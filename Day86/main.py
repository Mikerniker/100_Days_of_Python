from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#16425d"
MAX_LINE_LENGTH = 35  # Sets the maximum line length
correctly_typed = []
wrong = []

instructions = "Test your typing speed by typing each word you see in order " \
               "and clicking the space bar. When the one-minute timer " \
               "runs out, your typing speed in Words Per Minute (WPM) and " \
               "Characters Per Minute (CPM) will be displayed."

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

correctly_typed = []

correctly_typed = []
wrong = []

def compare_words(event):

    content = text_widget.get("1.0", "end-1c")  # Remove trailing newline character
    lines = content.split()

    # Highlight the first word
    end = text_widget.search(" ", "1.0", stopindex="end")
    text_widget.tag_add("start", "1.0", end)
    text_widget.tag_configure("start", background="#4d8f88",
                              foreground="white")

    if event.keysym == 'space':
        user_input = user_entry.get().strip().lower()
        target_word = lines[0]

        if target_word == user_input:
            text_widget.tag_configure("start", background="#58F139",
                                      foreground="black")
            correctly_typed.append(user_input)

        else:
            text_widget.tag_configure("start", background="red",
                                      foreground="black")
            wrong.append(user_input)


        # Delete the typed word from the text widget with a delay
        text_widget.after(50 * len(user_input), lambda: text_widget.delete("1.0", f"1.{len(target_word) + 1}"))
        user_entry.delete(0, END)  # Clear the entry for the next comparison



# Create the main window
window = Tk()
window.title("Mik's Speed Typing Test")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget with three rows
text_widget = Text(window, height=4.5, width=25,
                   wrap='word', font=("Georgia", 25))
text_widget.grid(column=0, row=3, rowspan=4, sticky="nsew")

insert_words()

instructions = "Test your typing speed by typing each word you see in order " \
               "and clicking the space bar. When the one-minute timer " \
               "runs out, your typing speed in Words Per Minute (WPM) and " \
               "Characters Per Minute (CPM) will be displayed."


# Load the image
typewriter = PhotoImage(file="typewriter.png")

# Create a Label for the image
image_label = Label(image=typewriter, bg=BACKGROUND_COLOR)
image_label.grid(column=1, row=2, pady=5, padx=10, sticky="W")

# Labels
header_label = Label(text="S p e e d  T y p i n g  T e s t",
                     font=("Georgia", 30, "bold"), fg="white",
                     bg=BACKGROUND_COLOR)
header_label.grid(column=0, row=1, pady=5)

# Entry
user_entry = Entry(width=30)
user_entry.grid(column=0, row=6, pady=10, ipadx=90, ipady=10)

# Run the Tkinter event loop
window.mainloop()