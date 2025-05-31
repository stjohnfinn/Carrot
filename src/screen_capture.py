import pyautogui
from PIL import Image
import numpy as np
import time

def capture_screen():
    try:
        screenshot = pyautogui.screenshot()
        return screenshot
    except Exception as e:
        print(f"Error capturing screen: {e}")
        return None
    
def get_game_screen():
  screenshot = capture_screen()

  path = f"screenshots/screenshot_{int(time.time())}.png"

  if screenshot:
    width, height = screenshot.size
    # crop: (left, top, right, bottom)
    cropped_screenshot = screenshot.crop((0, 320, width, height-150))
    cropped_screenshot.save(path)
  
  return path

def isolate_score():
  screenshot = Image.open(get_game_screen())

  path = f"screenshots/screenshot_{int(time.time())}.png"

  width, height = screenshot.size
  cropped_screenshot = screenshot.crop((1300, 1410, width-1300, height-55))
  cropped_screenshot.save(path)

  return path

def isolate_digits():
  pass
