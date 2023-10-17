# This is in progress

from tkinter import *
import sys
from PIL import Image, ImageDraw, ImageFont

# Tktinter
window = tkinter.Tk()
window.title("Mik's Watermark")
window.minsize(width=800, height=500)
window.config(padx=20, pady=20)


# Ask the user to select a file
file_path = filedialog.askopenfilename()

image = Image.open(file_path)

#Canvas
canvas = Canvas(width=650, height=450, highlightthickness=0)
# Convert the Pillow image to a PhotoImage object
photo_img = ImageTk.PhotoImage(image)
canvas.create_image(325, 225, image=photo_img)
watermark_text = canvas.create_text(325, 225, text="", fill="white", font=("Arial", 35)) #adds watermark
canvas.grid(column=0, row=0, columnspan=2)


def add_watermark():
    watermark = input.get()
    canvas.itemconfig(watermark_text, text=watermark)


#Label
my_label = Label(text="Add name", font=("Arial", 14))
my_label.grid(column=0, row=1)

#Entry
input = Entry(width=30)
input.grid(column=1, row=1)

#Button
button = Button(text="Click me", command=add_watermark)
button.grid(column=2, row=1)


window.mainloop()