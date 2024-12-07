import pyautogui
import datetime

# Big Dinosaur dimensions
left = 37
top = 516
width = 187
height = 133

# Define the Dino region and region to right of dino
extra_width = 150  # width to the right of the dinosaur
right_region = (left + width, top, extra_width, height)

# Save the region screenshot reference
# timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


# Get browser window 
try:
    window = pyautogui.getWindowsWithTitle("Play Chrome Dinosaur Game Online - elgooG")[0]  
    window.activate()
except IndexError:
    print("Browser window not found. Make sure it's open.")
    exit() 


# Locate the dinosaur on the screen
try:
    locate_dinosaur = pyautogui.locateOnScreen('./images/dinosaur.png', confidence=0.7)
except pyautogui.ImageNotFoundException:
    print("Could not locate the image on the screen.")


# pyautogui.moveTo(100, 200)
# pyautogui.click()

# # Get the size of the primary monitor.
# screenWidth, screenHeight = pyautogui.size() 
