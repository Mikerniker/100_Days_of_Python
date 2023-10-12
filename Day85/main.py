# This is in progress

import tkinter
import sys
from PIL import Image, ImageDraw, ImageFont

# Tktinter
window = tkinter.Tk()
window.title("Mik's Watermark")
window.minsize(width=800, height=500)


#Label
my_label = tkinter.Label(text="Add Image to watermark", font=("Arial", 24, "bold"))
my_label.pack(expand=True)  #mylabel takes up whole space


window.mainloop()