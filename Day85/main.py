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


# Labels
image_label = Label(text="Select Image", font=("Arial", 12), fg="white", bg="#16425D")
image_label.grid(column=0, row=1, sticky="E", pady=6)

add_text_label = Label(text="Add Text", font=("Arial", 12), fg="white", bg="#16425D")
add_text_label.grid(column=0, row=2, sticky="E", pady=6)

show_text_label = Label(text="Show Text", font=("Arial", 12), fg="white", bg="#16425D")
show_text_label.grid(column=0, row=3, sticky="E", pady=6)

download_label = Label(text="Download", font=("Arial", 12), fg="white", bg="#16425D")
download_label.grid(column=0, row=4, sticky="E", pady=6)

font_family_label = Label(text="Font Family", font=("Arial", 10), fg="white", bg="#16425D")
font_family_label.grid(column=2, row=1, sticky="E", pady=6)

font_size_label = Label(text="Font Size", font=("Arial", 10), fg="white", bg="#16425D")
font_size_label.grid(column=2, row=2, sticky="E", pady=6)

font_color_label = Label(text="Font Color", font=("Arial", 10), fg="white", bg="#16425D")
font_color_label.grid(column=2, row=3, sticky="E", pady=6)


# Entry
watermark_entry = Entry(width=30)
watermark_entry.grid(column=1, row=2, sticky="W", padx=6)

# Button
choose_image_btn = Button(text="Select Image", command=replace_placeholder_image)
choose_image_btn.grid(column=1, row=1, sticky="W", padx=6)

show_text_btn = Button(text="Show Text", command=add_watermark)
show_text_btn.grid(column=1, row=3, sticky="W", padx=6)

# Create a Font dropdown menu
font_options_btn = OptionMenu(window, select_font, *all_fonts)
font_options_btn.grid(column=3, row=1, sticky="W", padx=6)

download_btn = Button(text="Download Image", command=save_watermark)
download_btn.grid(column=1, row=4, sticky="W", padx=6)

font_size_btn = OptionMenu(window, font_size_var, *font_size_options)
font_size_btn.grid(column=3, row=2, sticky="W", padx=6)

color_button = Button(window, text="Choose Color", command=choose_color)
color_button.grid(column=3, row=3, sticky="W", padx=6)

# Arrow buttons
up_img = Image.open("uparrow.png")
up_img = up_img.resize((20, 20), Image.LANCZOS)
up_button_img = ImageTk.PhotoImage(up_img)
up_button = Button(window, image=up_button_img, command=move_up, bg="#16425D")
up_button.grid(column=3, row=4)

down_img = Image.open("downarrow.png")
down_img = down_img.resize((20, 20), Image.LANCZOS)
down_button_img = ImageTk.PhotoImage(down_img)
down_button = Button(window, image=down_button_img, command=move_down, bg="#16425D")
down_button.grid(column=3, row=6)

left_img = Image.open("leftarrow.png")
left_img = left_img.resize((20, 20), Image.LANCZOS)
left_button_img = ImageTk.PhotoImage(left_img)
left_button = Button(window, image=left_button_img, command=move_left, bg="#16425D")
left_button.grid(column=2, row=5, sticky="E")

right_img = Image.open("rightarrow.png")
right_img = right_img.resize((20, 20), Image.LANCZOS)
right_button_img = ImageTk.PhotoImage(right_img)
right_button = Button(window, image=right_button_img, command=move_right, bg="#16425D")
right_button.grid(column=4, row=5, sticky="W")

window.mainloop()