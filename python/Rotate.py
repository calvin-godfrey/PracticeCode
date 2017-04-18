# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:59:53 2015

@author: ggodfrey
"""

import pygame as py
import sys
from pygame.locals import *
import pygame.gfxdraw as gfx
from math import cos, sin, pi, ceil, sqrt
from random import randint

py.init()
SCORE = 0
WIDTH = 600
HEIGHT = 800
DISPLAYSURF = py.display.set_mode((WIDTH, HEIGHT), 0, 32) #Sets image displayed
py.display.set_caption("Spinning Game!")#Title
MOVE_SPEED = 6
RED = (255, 0, 0)#COLORS
REDDER = (255, 150, 150)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
blue = (100, 100, 255)
black = (0, 0, 0)
white = (255, 255, 255)
fpsClock = py.time.Clock()#Allows for constant framerate
FPS = 60#60fps master race
COUNTER = 0#For figuring out where rotating ball is
DISPLAYSURF.fill(blue)

def myCirc(x, y, r, color, border): #So that I only have to call once to draw two circles
    gfx.aacircle(DISPLAYSURF, x, y, r, border)
    gfx.filled_circle(DISPLAYSURF, x, y, r, color)
    
def PointInCirc(x, y, r, a): #Figures out where the rotating cricle goes next frame
    return [x+r*sin(a*(pi/180.0)), y+r*-cos(a*(pi/180.0))]
    
def distance(x1, y1, x2, y2): #Distance formula! (collision)
    return sqrt((x1-x2)**2+(y1-y2)**2)
    
def DistancePointLine (px, py, x1, y1, x2, y2):
    LineMag = distance(x1, y1, x2, y2)

    if LineMag < 0.00000001:
        DistancePointLine = 9999
        return DistancePointLine

    u1 = (((px - x1) * (x2 - x1)) + ((py - y1) * (y2 - y1)))
    u = u1 / (LineMag * LineMag)

    if (u < 0.00001) or (u > 1):
        #// closest point does not fall within the line segment, take the shorter distance
        #// to an endpoint
        ix = distance(px, py, x1, y1)
        iy = distance(px, py, x2, y2)
        if ix > iy:
            DistancePointLine = iy
        else:
            DistancePointLine = ix
    else:
        # Intersecting point is on the line, use the formula
        ix = x1 + u * (x2 - x1)
        iy = y1 + u * (y2 - y1)
        DistancePointLine = distance(px, py, ix, iy)

    return DistancePointLine
class Circle: #Makes it easier to change and access features
    def __init__(self, x, y, r, color, border):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.border = border
        
class Rect:
    def __init__(self, x1, y1, width, height, color):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.color = color
        self.x2 = x1+width
        self.y2 = y1+height
        
testRect = Rect(randint(5, WIDTH-155), 20, 150, 100, white)
main = Circle(WIDTH/2, 600, 50, RED, black) #Want circles to be in mid of screen)
rotate = Circle(WIDTH/2, 530, 15, REDDER, black)

while True:
    for event in py.event.get():
        if event.type == QUIT:
            py.display.quit()
            sys.exit()
            
    keys = py.key.get_pressed() #Figures out which keys are pressed down
    #The way it was before you couldn't hold down buttons
    if keys[K_UP] or keys[K_w]:
        if main.r >= 200:
            main.r = main.r
        main.r = int(ceil(main.r*1.03)) #Grows exponentially, looks better
    elif keys[K_DOWN] or keys[K_s]:
        if main.r < 300:
            main.r = int(main.r*0.97)#Slower if bigger, faster if smaller
        else:
            main.r = int(main.r*0.98)
    if main.r < 5: #Set min radius so that it doesn't become tiny point
        main.r = 5
        
        
    COUNTER += 3 #Moves 3° around circle per tick (maybe a little fast)
    angle = COUNTER % 360 #So that counter doesn't have to reset
    points = PointInCirc(main.x, main.y, main.r-rotate.r, angle) #Returns array
    rotate.x = points[0] #Sets circle attributes at new points
    rotate.y = points[1]
    if COUNTER % 10 == 0:
        rotate.x += 0
    if DistancePointLine(rotate.x, rotate.y, testRect.x1, testRect.y2, testRect.x2, testRect.y2) < rotate.r or \
    DistancePointLine(rotate.x, rotate.y, testRect.x2, testRect.y1, testRect.x2, testRect.y2) < rotate.r:
        print "GAME OVER"
        py.quit()
        sys.exit()
    if testRect.y1 > HEIGHT+10:
        testRect.y1 = 20
        testRect.y2 = testRect.y1 + testRect.height
        testRect.x1 = randint(5, WIDTH-(testRect.width+5))
        testRect.x2 = testRect.x1 + WIDTH
        SCORE += 1
    testRect.y1 += MOVE_SPEED
    testRect.y2 += MOVE_SPEED
    MY_FONT = py.font.Font('freesansbold.ttf', 32)
    MY_FONT_OBJ = MY_FONT.render('Score: ' + str(SCORE), True, GREEN, blue)
    MY_FONT_RECT = MY_FONT_OBJ.get_rect()
    MY_FONT_RECT.center = (20, 20)
    
    '''DRAWING STUFF AT THE VERY END'''
    DISPLAYSURF.fill(blue) #Draws new blank screen
    myCirc(main.x, main.y, main.r, main.color, rotate.border)
    myCirc(int(rotate.x), int(rotate.y), rotate.r, rotate.color, rotate.border) #Drawing function needs ints
    py.draw.rect(DISPLAYSURF, testRect.color, (testRect.x1, testRect.y1, testRect.width, testRect.height))
    DISPLAYSURF.blit(MY_FONT_OBJ, MY_FONT_RECT)    
    
    #TODO add obstacles
    py.display.update() #Not sure what they do but I need them
    fpsClock.tick(FPS)
py.quit()