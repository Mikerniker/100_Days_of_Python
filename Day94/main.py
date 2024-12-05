import pyautogui
import datetime

# Big Dinosaur dimensions
left = 40
top = 517
width = 187
height = 133

# Define the Dino region and region to right of dino
extra_width = 150  # width to the right of the dinosaur
combined_region = (left, top, width + extra_width, height)

# pyautogui.moveTo(100, 200)
# pyautogui.click()

# # Get the size of the primary monitor.
# screenWidth, screenHeight = pyautogui.size() 
