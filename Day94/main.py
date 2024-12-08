import pyautogui
import datetime
from PIL import ImageChops
import time

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

# "Game Over" region
game_over_region = (463, 423, 445, 38)

# Get browser window 
try:
    window = pyautogui.getWindowsWithTitle("Play Chrome Dinosaur Game Online - elgooG")[0]  
    window.activate()
except IndexError:
    print("Browser window not found. Make sure it's open.")
    exit() 


# Locate the dinosaur on the screen
locate_dinosaur = pyautogui.locateOnScreen('./images/dinosaur.png', confidence=0.7)
if locate_dinosaur is None:
    print("Could not locate the dinosaur on the screen.")
    exit()

# Start the game
pyautogui.press('space')
print(f"Dinosaur found at: {locate_dinosaur}")
time.sleep(2)

# Get initial screenshot
initial_screenshot = pyautogui.screenshot(region=right_region)
initial_screenshot.save("initial_screenshot.png")
locate_dinosaur2 = pyautogui.locateOnScreen('./images/dinosaur2.png', confidence=0.7)

game_over = False

while not game_over:
    # Take a new screenshot of the detection zone
    current_screenshot = pyautogui.screenshot(region=right_region)

    diff = ImageChops.difference(initial_screenshot, current_screenshot)

    ##


    # Take a new screenshot of the "Game Over" region
    game_over_screenshot = pyautogui.screenshot(region=game_over_region)