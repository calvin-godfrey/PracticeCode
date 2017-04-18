# -*- coding: utf-8 -*-
"""
Windows only
"""
import time as t
import win32api as api
import win32con as con

def autoRightClick():
    """Holds the mouse down"""
    coords = list(api.GetCursorPos())
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN, coords[0], coords[1], 0, 0)
    t.sleep(0.05)#Holds down the mouse
    api.mouse_event(con.MOUSEEVENTF_RIGHTUP, coords[0], coords[1], 0, 0)

def autoLeftClick():
    """Holds the mouse down"""
    coords = list(api.GetCursorPos())
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN, coords[0], coords[1], 0, 0)
    t.sleep(0.01)#Holds down the mouse
    api.mouse_event(con.MOUSEEVENTF_LEFTUP, coords[0], coords[1], 0, 0)

def rightClick(x, y):
    """Clicks at given coordinates"""
    api.SetCursorPos((x/40, y/54))
    t.sleep(0.05)
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN|con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_RIGHTUP|con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

def leftClick(x, y):
    """Clicks at given coordinates"""
    api.SetCursorPos((x/40, y/54))
    t.sleep(0.05)
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN|con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_LEFTUP|con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

def dragLeft(x1, y1, x2, y2):
    deltaX = (x2-x1)/20.0
    deltaY = (y2-y1)/20.0
    api.SetCursorPos((x1, y1))
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN|con.MOUSEEVENTF_ABSOLUTE, x1, y1, 0, 0)
    for i in range(1, 21):
        t.sleep(0.01)
        api.SetCursorPos(((int(x1+(deltaX*i)), int(y1+(deltaY*i)))))
    api.mouse_event(con.MOUSEEVENTF_LEFTUP|con.MOUSEEVENTF_ABSOLUTE, x2, y2, 0, 0)

def typeLetter(letter):
    if letter in "/.,":
        x = ord(letter)+144+32 #Difference between ord() and what the function wants
    else:
        x = ord(letter)
    api.keybd_event(x-32, 0, con.KEYEVENTF_EXTENDEDKEY, 0)
    api.keybd_event(x-32, 0, con.KEYEVENTF_KEYUP, 0)

def typeLettersTime(letters, time): #Letters is an array
    for letter in letters:
        if letter in ",.":
            x = ord(letter)+144+32
        elif letter in "1234567890":
            x = ord(letter)+32
        else:
            x = ord(letter)
        api.keybd_event(x-32, 0, con.KEYEVENTF_EXTENDEDKEY, 0)
    t.sleep(time)
    for letter in letters[::-1]:
        if letter in ",.":
            x = ord(letter)+144+32
        elif letter in "1234567890":
            x = ord(letter)+32
        else:
            x = ord(letter)
        api.keybd_event(x-32, 0, con.KEYEVENTF_KEYUP, 0)

def typeLetterTime(letter, time):
    if letter in "/,.":
        x = ord(letter)+144+32
    elif letter in "123567890":
        x = ord(letter)+32
    else:
        x = ord(letter)
    api.keybd_event(x-32, 0, con.KEYEVENTF_EXTENDEDKEY, 0)
    t.sleep(time)
    api.keybd_event(x-32, 0, con.KEYEVENTF_KEYUP, 0)


def getCursor(delay):
    t.sleep(delay)
    return list(api.GetCursorPos())
