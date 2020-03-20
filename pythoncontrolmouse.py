import pyautogui

#allows mouse to go to corners of the screen without breaking program
pyautogui.FAILSAFE = False

import win32api
import time

#full credit to Kevin from stackoverflow here: https://stackoverflow.com/questions/13380938/pygame-capture-keyboard-events-when-window-not-in-focus
def isKeyPressed(key):
    #"if the high-order bit is 1, the key is down; otherwise, it is up."
    return (win32api.GetKeyState(key) & (1 << 7)) != 0


#Look up virtual keys here: https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN

LEFT_ARROW = 0x25
UP_ARROW = 0x26
RIGHT_ARROW = 0x27
DOWN_ARROW = 0x28
SHIFT = 0xA0
CTRL = 0xA2

#program key binds

moveLeftKey = ord('J')
moveRightKey = ord('L')
moveUpKey = ord('I')
moveDownKey = ord('K')
slowdown1Key = CTRL
slowdown2Key = SHIFT


def move(x, y):
    if(abs(x)+abs(y) > 0.01):
        print("moving mouse {0}, {1}".format(x,y))
    pyautogui.moveRel(x,y)


speed = 200.0


print("program started")

while True:
    x = 0.0
    y = 0.0

    if(isKeyPressed(moveLeftKey)):
        x -= speed
    
    if(isKeyPressed(moveRightKey)):
        x += speed

    if(isKeyPressed(moveDownKey)):
        y += speed

    if(isKeyPressed(moveUpKey)):
        y -= speed

    if(isKeyPressed(slowdown1Key)):
        x*=0.75
        y*=0.75

    if(isKeyPressed(slowdown2Key)):
        x*=0.5
        y*=0.5
    
    move(x, y)