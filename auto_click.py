from multiprocessing.connection import wait
import time

import pyautogui
import win32api
import win32con

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)

a = 0
game = None

start = None
start2 = None
start3 = None
start4 = None
while game is None:
    game = pyautogui.locateCenterOnScreen('F:\Tai lieu tu may cu\Python_Project\game.png', region=(0, 0, 2560, 1080), grayscale=True, confidence=0.70)

    
pyautogui.moveTo(game)  # Moves the mouse to the coordinates of the image
click()

while start is None:
    start = pyautogui.locateCenterOnScreen('F:\Tai lieu tu may cu\Python_Project\TFT.png', region=(0, 0, 2560, 1080), grayscale=True, confidence=0.70)
pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
click()
time.sleep(10)

while start2 is None:
    start2 = pyautogui.locateCenterOnScreen('F:\Tai lieu tu may cu\Python_Project\play_tft.png', region=(0, 0, 2560, 1080), grayscale=True,confidence=0.70)
pyautogui.moveTo(start2)
click()

while start3 is None:
    start3 = pyautogui.locateCenterOnScreen('F:\Tai lieu tu may cu\Python_Project\match_find.png', region=(0, 0, 2560, 1080), grayscale=True, confidence=0.70)
pyautogui.moveTo(start3)
click()
    
while start4 is None:

    start4 = pyautogui.locateCenterOnScreen('F:\Tai lieu tu may cu\Python_Project\match_accept.png', region=(0, 0, 2560, 1080), grayscale=True, confidence=0.70)

pyautogui.moveTo(start4)  # Moves the mouse to the coordinates of the image
click()






                

    
                    
                

        
