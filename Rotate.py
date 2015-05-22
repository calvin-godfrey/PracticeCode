# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:59:53 2015

@author: ggodfrey
"""

import pygame as py
import sys
from pygame.locals import *
import pygame.gfxdraw as gfx
from math import cos, sin, pi, ceil

py.init()
DISPLAYSURF = py.display.set_mode((400, 800), 0, 32)
py.display.set_caption("Spinning Game!")
RED = (255, 0, 0)
REDDER = (255, 150, 150)
blue = (100, 100, 255)
fpsClock = py.time.Clock()
FPS = 60
COUNTER = 0
DISPLAYSURF.fill(blue)
RIGHT = K_RIGHT
LEFT = K_LEFT
def myCirc(x, y, r, color):
    gfx.aacircle(DISPLAYSURF, x, y, r, color)
    gfx.filled_circle(DISPLAYSURF, x, y, r, color)
def PointInCirc(x, y, r, a):
    return [x+r*sin(a*(pi/180.0)), y+r*-cos(a*(pi/180.0))]

class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        
main = Circle(200, 600, 50, RED)
rotate = Circle(200, 530, 15, REDDER)
myCirc(main.x, main.y, main.r, main.color)
myCirc(rotate.x, rotate.y, rotate.r, rotate.color)

print PointInCirc(200, 600, 50, 10)

while True:
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_UP] or keys[K_w]:
        main.r = int(ceil(main.r*1.03))
    elif keys[K_DOWN] or keys[K_s]:
        main.r = int(main.r*0.97)
    if main.r < 5:
        main.r = 5
    COUNTER += 3
    angle = COUNTER % 360
    points = PointInCirc(main.x, main.y, main.r+rotate.r, angle)
    rotate.x = points[0]
    rotate.y = points[1]
    DISPLAYSURF.fill(blue)
    myCirc(int(rotate.x), int(rotate.y), rotate.r, rotate.color)
    myCirc(main.x, main.y, main.r, main.color)
    py.display.update()
    fpsClock.tick(FPS)