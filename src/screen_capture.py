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

def isolate_score(image):
  pass

def isolate_digits(image):
  pass

def digit_to_number(digit_image):
  pass
