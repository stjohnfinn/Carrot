import pygame
import time

def play_sound(mp3_file_path, wait=True):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play()
    
    if wait:
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

def stop_sound():
    pygame.mixer.music.stop()
