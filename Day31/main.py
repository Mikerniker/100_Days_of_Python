from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50,  pady=50, bg=BACKGROUND_COLOR)


rand_word = {}
words_dict = {}

try:
    words = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_words = pandas.read_csv("data/french_words.csv")
    words_dict = original_words.to_dict(orient="records")
else:
    words_dict = words.to_dict(orient="records")


def word_access():
    global rand_word, change_card
    window.after_cancel(change_card)
    rand_word = random.choice(words_dict)
    french_word = rand_word['French']
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(translation_text, text=french_word, fill="black")
    canvas.itemconfig(current_image, image=front_img)
    change_card = window.after(3000, flip_card)


def right_click():
    words_dict.remove(rand_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    word_access()


def flip_card():
    global rand_word
    english_word = rand_word['English']
    canvas.itemconfig(language_text, text="English", fill="#fff")
    canvas.itemconfig(translation_text, text=english_word, fill="#fff")
    canvas.itemconfig(current_image, image=back_img)


change_card = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
current_image = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
translation_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


canvas.grid(column=0, row=0, columnspan=2)

#BUTTONS

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_click)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=word_access)
wrong_button.grid(column=1, row=1)


word_access()

window.mainloop()
