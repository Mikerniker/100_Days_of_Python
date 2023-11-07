# Day 85 Image Watermarking App

## Overview

- Topics: Tkinter, PIL library

### The challenge

- Create a desktop application with a Graphical User Interface (GUI) where you can upload an image and use Python to add a watermark.

### Links

- Solution URL: [Image Watermarking App](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day85)

## Notes
**Approach**
My approach to building a GUI watermark app with Python involves breaking down the problem into several parts. First, I create a graphical user interface using Tkinter. I then implemented the functionality for the user to select an image. Next, I added options for customizing the watermark, such as adding font size, font colors, and the ability to position the watermark. Finally, apply the watermark to the selected image and allow the user to save the resulting image. 
This took me some time to build, and had to use ChatGPT to help me debug as well as lookup some methods in Tkinter and PIL. Even with this, there were several limitations since ChatGPT sometimes hallucinates and or has some outdated information on some of the libraries (at least for the free version). 

**For Improvement:** 
I would like to add more features in the future, like the ability to adjust opacity and rotation of the watermark. I would also like to improve on the user-friendliness and intuitiveness of the interface, making it easier for users to navigate and use the application.

**Biggest learning:**
- I learned how to resize an image to a desired size, using the Python Imaging Library (PIL) and the `resize` method. Also found that the 'ANTIALIAS' filter is no longer available (ChatGPT recommended), so I used the 'LANCZOS' filter instead.

- Reviewed how to save a file with  `file dialog` in Tkinter, which allows users to specify the format and location for saving the watermarked image. 

- Learned how to align text or buttons on the GUI using the 'sticky' parameter in the grid layout. Example: `font_family_label.grid(column=2, row=1, sticky="E", pady=6)`

- Reviewed how to change the background color of the Tkinter window, ie set the background color with the `.bg` property. Example: `show_text_label = Label(text="Show Text", font=("Arial", 12), fg="white", bg="#16425D")`

- Learned how to capture a screenshot of the entire window or a specific portion of the screen using the `ImageGrab.grab()` method from the PIL library. 
