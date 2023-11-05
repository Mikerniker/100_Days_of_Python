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

# FONT FAMILY: Create font family menu dropdown options
font_families = font.families()
all_fonts = []
for family in font_families:
    all_fonts.append(family)

# Datatype of menu text
select_font = StringVar()

# initial menu text
select_font.set(all_fonts[11])

# FONT SIZE: Create a font size variable and a dropdown menu
font_size_var = StringVar()
font_size_var.set("12")  # Default font size
font_size_options = [size for size in range(8, 96)]


def load_image():
    global file_path
    file_path = filedialog.askopenfilename()


def replace_placeholder_image():
    global photo_img
    # Load the filepath
    load_image()
    new_image = Image.open(file_path)

    if new_image:
        resized_new_image = new_image.resize((CANVAS_WIDTH, CANVAS_HEIGHT),
                                             Image.LANCZOS)
        photo_img = ImageTk.PhotoImage(resized_new_image)
        canvas.itemconfig(image_to_watermark, image=photo_img)


def change_font_size():
    """Function to change the text font size"""
    selected_size = int(font_size_var.get())
    return selected_size


def choose_color():
    """Function to change the text color"""
    global selected_color
    color = colorchooser.askcolor()
    if color:
        selected_color = color[1]
        print("Selected color:", selected_color)


def add_watermark():
    """Function to add a watermark """
    if selected_color is not None:
        watermark = watermark_entry.get()
        selected_font_family = select_font.get()
        selected_font_size = change_font_size() #25
        font_specs = Font(family=selected_font_family, size=selected_font_size)
        canvas.itemconfig(watermark_text, text=watermark,
                          fill=selected_color, font=font_specs)
        canvas.coords(watermark_text, cursor_x, cursor_y)  # Set text position
    else:
        messagebox.showwarning(title="Add Color",
                               message="Please choose a color first.")
        print("Please choose a color first.")


def save_watermark():
    """Saves final watermark image"""
    # Get the coordinates of the canvas
    x0 = canvas.winfo_rootx()
    y0 = canvas.winfo_rooty()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()

    screenshot = ImageGrab.grab(bbox=(x0, y0, x1, y1))

    # Ask the user for the file path to save the image
    file_path = filedialog.asksaveasfilename(
        confirmoverwrite=True,
        defaultextension=".png",
        filetypes=[("JPEG", ".jpg"), ("PNG", ".png"),
                   ("Bitmap", ".bmp"), ("GIF", ".gif")])

    if file_path:
        screenshot.save(file_path)
        messagebox.showinfo("Success",
                            f"The watermarked image has been saved as"
                            f" {file_path}")


def move_up():
    """Function to move button up when arrow button is pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, 0, -5)
    cursor_y -= 5


def move_down():
    """Function to move button down when arrow button is pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, 0, 5)
    cursor_y += 5


def move_left():
    """Function to move button left when arrow button is pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, -5, 0)
    cursor_x -= 5


def move_right():
    """Function to move button right when arrow button is pressed"""
    global cursor_x, cursor_y
    canvas.move(watermark_text, 5, 0)
    cursor_x += 5

# NOtE TO SELF REVIEW FROM HERE







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