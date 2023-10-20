# This is in progress

from tkinter import *
import sys
from PIL import Image, ImageDraw, ImageFont

# Tktinter
window = Tk()
window.title("Mik's Watermark")
window.minsize(width=800, height=500)
window.config(padx=20, pady=20)


# Ask the user to select a file
file_path = filedialog.askopenfilename()

image = Image.open(file_path)

#Canvas
canvas = Canvas(width=650, height=450, highlightthickness=0)
watermark_holder = PhotoImage(file="Watermarkme.png")
image_to_watermark = canvas.create_image(325, 225, image=watermark_holder)  #image=photo_img
watermark_text = canvas.create_text(325, 225, text="", fill="white", font=("Arial", 35)) #adds watermark
canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")


def add_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        photo_img = ImageTk.PhotoImage(image)
        canvas.itemconfig(image_to_watermark, image=photo_img)
        add_image.photo_img = photo_img

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
button1 = Button(text="Select Image", command=add_image)
button1.grid(column=1, row=1)

button2 = Button(text="Click me", command=add_watermark)
button2.grid(column=2, row=2)

button3 = Button(text="Download Image", command=add_watermark)
button3.grid(column=2, row=3)


window.mainloop()