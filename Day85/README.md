# Day 85 Image Watermarking App


https://github.com/Mikerniker/100_Days_of_Python/assets/63586831/a7ea6114-37ee-4e68-a511-8cad5af18634

Note: My screen recorder doesn't record the pop-ups. :(

## Overview

- Topics: Tkinter, PIL library

### The challenge

- Create a desktop application with a Graphical User Interface (GUI) where you can upload an image and use Python to add a watermark.

### Links

- Solution URL: [Image Watermarking App](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day85)

## Notes
**Approach**
First, I tried breaking down the problem into several parts. I created a graphical user interface using Tkinter. I then implemented the functionality for the user to select an image. Next, I added options for customizing the watermark, such as adding font size, font colors, and the ability to position the watermark. Finally,I  applied the watermark to the selected image and added an option for the user to save the resulting image. This took some time to build, even with the aid of ChatGPT, since it sometimes hallucinated and or had some outdated information on some of the libraries (at least for the free version). 

**For Improvement:** 
I would like to add more features in the future, like the ability to adjust opacity and rotation of the watermark. I would also like to improve on the user-friendliness and intuitiveness of the interface, making it easier for users to navigate and use the application.

**Biggest learning:**
- I learned how to resize an image to a desired size, using the Python Imaging Library (PIL) and the `resize` method. Also found that the 'ANTIALIAS' filter is no longer available (ChatGPT recommended), so I used the 'LANCZOS' filter instead.

- Reviewed how to save a file with  `file dialog` in Tkinter, which allows users to specify the format and location for saving the watermarked image. 

- Learned how to align text or buttons on the GUI using the 'sticky' parameter in the grid layout. Example: `font_family_label.grid(column=2, row=1, sticky="E", pady=6)`

- Reviewed how to change the background color of the Tkinter window, ie set the background color with the `.bg` property. Example: `show_text_label = Label(text="Show Text", font=("Arial", 12), fg="white", bg="#16425D")`

- Learned how to capture a screenshot of the entire window or a specific portion of the screen using the `ImageGrab.grab()` method from the PIL library. 
