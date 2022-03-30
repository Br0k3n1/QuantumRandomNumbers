from inspect import classify_class_attrs
from win32api import GetKeyState
import threading
from pygame import time
import mouse

cps = 120

triggerKey = 0x46 # f

clicking = False

# Check if Key Down
def key_down(key):
        state = GetKeyState(key) 
        if (state != 0) and (state != 1):
            return True
        else:
            return False

# Check if Key Up
def key_up(key):
    keystate = GetKeyState( key )
    if (keystate == 0) or (keystate == 1):
        return True
    else:
        return False

# Checks if trigger key has been pressed
def checker():
    global clicking 
    while True:
        if key_down(triggerKey):
            while key_up(triggerKey) == False:
                pass
            if clicking == False:
                clicking = True
            elif clicking == True:
                clicking = False

# Creates thread that checks keyboard
def keyboard_checker():
    th = threading.Thread(target=checker)
    th.start()

# Initiate thread that checks keyboard
keyboard_checker()

# Create Clock from pygame
clock = time.Clock()

while True:
    clock.tick(cps) # limit loops per second
    print(clicking)
    if clicking:
        mouse.click("left")