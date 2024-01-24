from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#16425d"
MAX_LINE_LENGTH = 35  # Sets the maximum line length
correctly_typed = []
wrong = []
countdown_ended = False


instructions = "Test your typing speed by typing each word you see in order " \
               "and clicking the space bar. When the one-minute timer " \
               "runs out, your typing speed in Words Per Minute (WPM) and " \
               "Characters Per Minute (CPM) will be displayed."

def insert_words():
    words = pandas.read_csv("common_english_words.csv")
    words_list = words['Common Words'].tolist()
    words_to_type = [random.choice(words_list) for _ in range(150)]
    print(words_to_type)

    for word in words_to_type:
        text_widget.insert("1.0", word + " ")

        text_widget.tag_configure("center", justify="center")
        text_widget.tag_add("center", "1.0", "end")


def compare_words(event):
    content = text_widget.get("1.0", "end-1c")  # Remove trailing newline character
    lines = content.split()

    if not countdown_ended:
        # Highlight the first word
        end = text_widget.search(" ", "1.0", stopindex="end")
        text_widget.tag_add("start", "1.0", end)
        text_widget.tag_configure("start", background="#4d8f88", foreground="white")
        
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


def countdown(time_sec):
    global countdown_ended

    matched = 0

    if time_sec >= 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=f"Time Left: {timeformat}")
        window.after(1000, countdown, time_sec - 1)

    else:
        countdown_ended = True
        for word in correctly_typed:
            matched += len(word)
        word_per_min = matched / 5

        CPM_label.config(text=f"Corrected CPM: {matched}")
        words_per_minute_label.config(text=f"Words Per Minute: {word_per_min}")
        errors_label.config(text=f"Total Errors: {len(wrong)}")

        #INSTRUCTIONS LABEL
        instructions_label.config(text="Your Typing Speed:",
                                  font=("Georgia", 28, "bold"), fg="white",
                                  bg=BACKGROUND_COLOR)


        text_widget.delete('1.0', END)

        final_scores = f"Corrected CPM: {matched} \n" \
                       f"Words Per Minute: {word_per_min}\n" \
                       f"Total Errors: {len(wrong)}"
        text_widget.insert("1.0", final_scores)
        text_widget.tag_configure("center", justify="center")
        text_widget.tag_add("center", "1.0", "end")


def reset_labels():
    """Resets all the labels"""
    global countdown_ended

    countdown_ended = False
    user_entry.delete(0, END)
    time_label.config(text="Time Left: 01:00")
    CPM_label.config(text=f"Corrected CPM: 0")
    words_per_minute_label.config(text=f"Words Per Minute: 0")
    instructions_label = Label(text=instructions, font=("Arial", 11),
                               wraplength=text_widget.winfo_reqwidth(),
                               justify="center", fg="white",
                               bg=BACKGROUND_COLOR)
    errors_label.config(text=f"Total Errors: 0")
    insert_words()
    countdown(60)

# Create the main window
window = Tk()
window.title("Mik's Speed Typing Test")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget with three rows
text_widget = Text(window, height=4.5, width=25,
                   wrap='word', font=("Georgia", 25))
text_widget.grid(column=0, row=3, rowspan=4, sticky="nsew")

insert_words()

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

instructions_label = Label(text=instructions, font=("Arial", 11),
                           wraplength=text_widget.winfo_reqwidth(),
                           justify="center", fg="white", bg=BACKGROUND_COLOR)
instructions_label.grid(column=0, row=2, pady=5)

time_label = Label(text="Time Left: 01:00", font=("Arial", 12), fg="white", bg=BACKGROUND_COLOR)
time_label.grid(column=1, row=3, sticky="E", pady=6)

CPM_label = Label(text="Corrected CPM: 0", font=("Arial", 12), fg="white", bg=BACKGROUND_COLOR)
CPM_label.grid(column=1, row=4, sticky="E", pady=6)

words_per_minute_label = Label(text="Words Per Minute: 0",
                               font=("Arial", 12), fg="white",
                               bg=BACKGROUND_COLOR)
words_per_minute_label.grid(column=1, row=5, sticky="E", pady=6)

errors_label = Label(text="Total Errors: 0", font=("Arial", 12),
                     fg="white", bg=BACKGROUND_COLOR)
errors_label.grid(column=1, row=6, sticky="E", pady=6)


# Entry
user_entry = Entry(width=30)
user_entry.grid(column=0, row=7, pady=10, ipadx=90, ipady=10)


# Bind the KeyRelease event to compare_word
user_entry.bind("<KeyRelease>", compare_words) 

# Button
restart_btn = Button(text="Restart", command=reset_labels)
restart_btn.grid(column=1, row=7, pady=10, ipadx=20, ipady=10, sticky="E")

# Call the countdown
countdown(60)


# Run the Tkinter event loop
window.mainloop()