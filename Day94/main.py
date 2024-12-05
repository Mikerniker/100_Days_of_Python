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

# Save the region screenshot reference
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_path = f"combined_region_{timestamp}.png"

# Get browser window 
try:
    window = pyautogui.getWindowsWithTitle("Play Chrome Dinosaur Game Online - elgooG")[0]  
    window.activate()
except IndexError:
    print("Browser window not found. Make sure it's open.")
    exit() 

# pyautogui.moveTo(100, 200)
# pyautogui.click()

# # Get the size of the primary monitor.
# screenWidth, screenHeight = pyautogui.size() 
