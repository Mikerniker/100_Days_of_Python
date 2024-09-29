import pyautogui
from PIL import Image
import webbrowser

# Open the game URL
webbrowser.open("https://elgoog.im/t-rex/")

pyautogui.moveTo(100, 200)
pyautogui.click()

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size() 
