# This is in progress

from tkinter import *
import sys
from tkinter import filedialog
from tkinter import font, colorchooser, messagebox
from tkinter.font import Font
from PIL import Image, ImageDraw, ImageFont, ImageTk


# Tktinter
window = Tk()
window.title("Mik's Watermark")
window.config(padx=20, pady=20)


# Ask the user to select a file
file_path = filedialog.askopenfilename()
image = Image.open(file_path)

#Canvas
canvas = Canvas(width=800, height=500, highlightthickness=0)
watermark_holder = PhotoImage(file="Watermarkme.png")
image_to_watermark = canvas.create_image(400, 250, image=watermark_holder)  #image=photo_img
watermark_text = canvas.create_text(325, 225, text="", fill="") #adds watermark
canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")


def add_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        max_size = (350, 350)  
        image.thumbnail(max_size) 
        photo_img = ImageTk.PhotoImage(image)
        canvas.itemconfig(image_to_watermark, image=photo_img)
        add_image.photo_img = photo_img


def add_watermark(event):
    if selected_color is not None:  # Check if a color has been selected
        watermark = input.get()
        selected_font_family = clicked.get()
        selected_font_size = change_font_size() 
        x, y = event.x, event.y  # Get the coordinates of the click  ADDED
        font_specs = Font(family=selected_font_family, size=selected_font_size)
        canvas.itemconfig(watermark_text, text=watermark, fill=selected_color,  font=font_specs)
        canvas.coords(watermark_text, x, y)  # Update the position of the text element  # ADDED
#     print("I got clicked")
    else:
        messagebox.showwarning(title="Add Color", message="Please choose a color first.")
        # print("Please choose a color first.")

# Get the available font families
font_families = font.families()
print(type(font_families))
all_fonts = []
for family in font_families:
    all_fonts.append(family)
print(all_fonts)

# Datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set(all_fonts[11])

# FONT SIZE: Create a font size variable and a dropdown menu
font_size_var = StringVar()
font_size_var.set("12")  # Default font size
font_size_options = [size for size in range(8, 96)]

selected_color = None

def change_font_size():
    """Function to change the text font size"""
    selected_size = int(font_size_var.get())
    return selected_size

# COLORS
def choose_color():
    global selected_color
    color = colorchooser.askcolor()  # This will open a color selection dialog
    if color:
        selected_color = color[1]
        print("Selected color:", selected_color)
       


#Label
label1 = Label(text="Select Image", font=("Arial", 12))
label1.grid(column=0, row=1)
label1.config(padx=5, pady=5)

label2 = Label(text="Add Text", font=("Arial", 12))
label2.grid(column=0, row=2)
label2.config(padx=5, pady=5)

label3 = Label(text="Add Watermark", font=("Arial", 12))
label3.grid(column=0, row=3)
label3.config(padx=5, pady=5)

label4 = Label(text="Download", font=("Arial", 12))
label4.grid(column=0, row=4)
label4.config(padx=5, pady=5)

label5 = Label(text="Choose Font", font=("Arial", 10))
label5.grid(column=2, row=1)

label6 = Label(text="Choose Color", font=("Arial", 10))
label6.grid(column=2, row=2)

#Entry
input = Entry(width=30)
input.grid(column=1, row=2)


#Button
button1 = Button(text="Select Image", command=add_image)
button1.grid(column=1, row=1)

button2 = Button(text="Add Watermark", command=add_watermark)
button2.grid(column=1, row=3)




window.mainloop()