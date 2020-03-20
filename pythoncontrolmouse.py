import pyautogui
import win32api
import time

def keyWasUnPressed():
    print("enabling joystick...")
    #enable joystick here

def keyWasPressed():
    print("disabling joystick...")
    #disable joystick here

def isKeyPressed(key):
    #"if the high-order bit is 1, the key is down; otherwise, it is up."
    return (win32api.GetKeyState(key) & (1 << 7)) != 0

LEFT_ARROW = ord('J')#0x25
UP_ARROW = ord('I')#0x26
RIGHT_ARROW = ord('L')#0x27
DOWN_ARROW = ord('K')#0x28
SHIFT = 0xA0
CTRL = 0xA2

pyautogui.FAILSAFE = False

def move(x, y):
    if(abs(x)+abs(y) > 0.01):
        print("moving mouse {0}, {1}".format(x,y))
    pyautogui.moveRel(x,y)

base_speed = 100.0

while True:
    x = 0.0
    y = 0.0

    if(isKeyPressed(LEFT_ARROW)):
        x -= base_speed
    
    if(isKeyPressed(RIGHT_ARROW)):
        x += base_speed

    if(isKeyPressed(DOWN_ARROW)):
        y += base_speed

    if(isKeyPressed(UP_ARROW)):
        y -= base_speed

    if(isKeyPressed(SHIFT)):
        x*=0.5
        y*=0.5
    elif(isKeyPressed(CTRL)):
        x*=2
        y*=2
    
    move(x, y)