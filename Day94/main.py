import pyautogui
import datetime

# Big Dinosaur dimensions
left = 40
top = 517
width = 187
height = 133

# Define the Dino region and region to right of dino
extra_width = 150  # width to the right of the dinosaur
right_region = (left + width, top, extra_width, height)

# Save the region screenshot reference
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_path = f"combined_region_{timestamp}.png"


def check_for_obstacles():
    """Detect obstacles and trigger a jump if necessary."""
    # Initial State Screenshot
    initial_screenshot = pyautogui.screenshot(screenshot_path, region=right_region)
    print(f"Screenshot of the right region saved as {screenshot_path}")
    # Save screenshot for debugging (optional)
    initial_screenshot.save("detection_zone.png")
    
    obstacle_positions = []  # Store detected obstacle coordinates
    #continue for later


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
