import numpy
import pyautogui
import cv2
import time
import keyboard
from time import gmtime, strftime
from datetime import datetime
import random
import win32gui

unter = None
holz = None
jagg = None
pfl = None
stein = None
angeln = None


if __name__ == "__main__":

    while keyboard.is_pressed('q') == False:
        
        
        #unter = pyautogui.locateOnScreen('unter.png', confidence=0.8, region=(873, 440, 80, 74))
        #unter = pyautogui.locateOnScreen('unter.png', confidence=0.8)
        
        #holz = pyautogui.locateOnScreen('holz.png', confidence=0.8)
        
        jagg = pyautogui.locateOnScreen('jagg.png', confidence=0.8)
        
        #pfl = pyautogui.locateOnScreen('pfl.png', confidence=0.8)
        
        #stein = pyautogui.locateOnScreen('stein.png', confidence=0.8)
        
        #angeln = pyautogui.locateOnScreen('angeln.png', confidence=0.8)
        
        if unter is not None or holz is not None or jagg is not None or pfl is not None or angeln is not None:
                     
            print("found")
            time.sleep(random.uniform(0.2, 0.8))
            pyautogui.keyDown('g')
            time.sleep( random.uniform( 0.01, 0.05 )) # vorher (0.05, 0.1)
            pyautogui.keyUp('g')
            time.sleep(3)
            
                    # pyautogui.press('space')