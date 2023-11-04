# This is in progress

from tkinter import *
from tkinter import filedialog, font, colorchooser, messagebox
from tkinter.font import Font
from PIL import Image, ImageTk, ImageGrab


# Tkinter
window = Tk()
window.title("Mik's Watermark")
window.config(padx=20, pady=20)
window['background'] ='#16425D'

# Global Variables
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500
file_path = ""
photo_img = None
selected_color = None
cursor_x = 325
cursor_y = 200

#Canvas
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
placeholder_image = PhotoImage(file="Watermarkme.png")
image_to_watermark = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2,
                                         anchor=CENTER, image=placeholder_image)
watermark_text = canvas.create_text(325, 200, text="", fill="") #adds text watermark
canvas.grid(row=0, column=0, columnspan=5, sticky="nsew")


def load_image():
    """Function to ask the user to select a file"""
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        original_width, original_height = image.size  
       
        # Calculate new dimensions to fit within the canvas while maintaining the aspect ratio
        new_width = canvas_width
        new_height = (original_height * new_width) // original_width  #ADDED

        if new_height > canvas_height:
            new_height = canvas_height
            new_width = (original_width * new_height) // original_height

        resized_image = image.resize((new_width, new_height), Image.LANCZOS)

        # Calculate the position to center the image on the canvas
        x = (canvas_width - new_width) // 2
        y = (canvas_height - new_height) // 2

        photo_img = ImageTk.PhotoImage(resized_image)
        return photo_img, x, y


def add_image(photo_img=None, x=None, y=None):
    """Function to add an image to the canvas"""
    if photo_img:
        canvas.itemconfig(image_to_watermark, image=photo_img)
        if x is not None and y is not None:
            canvas.coords(image_to_watermark, x, y)
        add_image.photo_img = photo_img  # Store the PhotoImage to prevent it from being garbage collected


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

# Global variables to store cursor coordinates
cursor_x = 325
cursor_y = 200


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
        #print("Selected color:", selected_color)

def move_up():
    """Function to move button cursor up when arrow buttons keys are pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, 0, -5)
    cursor_y -= 5

def move_down():
    """Function to move button cursor down when arrow buttons are pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, 0, 5)
    cursor_y += 5

def move_left():
    """Function to move button cursor when arrow keys are pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, -5, 0)
    cursor_x -= 5

def move_right():
    """Function to move button cursor when arrow keys are pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, 5, 0)
    cursor_x += 5

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

# Create Dropdown menu
font_options = OptionMenu(window, select_font, *all_fonts)
font_options.grid(column=3, row=1)

button3 = Button(text="Download Image", command=save_watermark)
button3.grid(column=1, row=4)

font_size_menu = OptionMenu(window, font_size_var, *font_size_options)
font_size_menu.grid(column=3, row=2)

apply_color_button = Button(window, text="Apply", command=change_font_size)
apply_color_button.grid(column=4, row=2)

color_button = Button(window, text="Choose Color", command=choose_color)
color_button.grid(column=3, row=3)

window.mainloop()