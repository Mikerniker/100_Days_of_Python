# This is in progress

import tkinter
import sys
from PIL import Image, ImageDraw, ImageFont

# Tktinter
window = tkinter.Tk()
window.title("Mik's Watermark")
window.minsize(width=800, height=500)
window.config(padx=20, pady=20)


#Canvas
canvas = Canvas(width=650, height=450, highlightthickness=0)
burger_img = PhotoImage(file="hamburger.png")
canvas.create_image(325, 225, image=burger_img)
canvas.create_text(325, 225, text="", fill="white", font=("Arial", 35)) #adds watermark
canvas.grid(column=0, row=0, columnspan=2)




#Label
my_label = tkinter.Label(text="Add Image to watermark", font=("Arial", 24, "bold"))
my_label.pack(expand=True)  #mylabel takes up whole space


window.mainloop()