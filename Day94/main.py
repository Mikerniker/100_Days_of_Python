import pyautogui
import datetime
from PIL import ImageChops
import time

# Big Dinosaur dimensions
left = 37
top = 516
width = 187
height = 133
right = left + width

# Define detection zone dimensions
extra_width = 150  # width to the right of the dinosaur
right_region = (right, top, extra_width, height)

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
# print(f"Dinosaur found at: {locate_dinosaur}")
time.sleep(2)

# Get initial screenshot
initial_screenshot = pyautogui.screenshot(region=right_region)
initial_screenshot.save("initial_screenshot.png")
# locate_big_dinosaur = pyautogui.locateOnScreen('./images/dinosaur2.png', confidence=0.7)
#Note to self: locate_big_dinosaur was to get the coordinates for the big dinosaur 
# and determine the obstacle detection region beside it. (i.e.  Big Dinosaur dimensions above)

game_over = False

while not game_over:
    # Take a new screenshot of the detection zone
    current_screenshot = pyautogui.screenshot(region=right_region)

    # Compare screenshots
    diff = ImageChops.difference(initial_screenshot, current_screenshot)

    # Detect obstacle presence
    if diff.getbbox() is not None: 
        non_zero_count = sum(
            1 for pixel in diff.getdata() if pixel != (0, 0, 0))
        if non_zero_count > 500:
            pyautogui.press('up')  # Jump if there is a large pixel difference
            print(f"Jumped! Obstacle detected. Pixel difference: {non_zero_count}")

    # Take a new screenshot of the "Game Over" region
    game_over_screenshot = pyautogui.screenshot(region=game_over_region)
    try:
        check_gameover = pyautogui.locate('./images/game_over.png', game_over_screenshot, confidence=0.7)
        if check_gameover:
            game_over = True
            print("Game is over")
    except pyautogui.ImageNotFoundException:
        pass