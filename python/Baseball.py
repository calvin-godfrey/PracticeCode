# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 14:26:16 2014

@author: Home
"""
import urllib2 as u
import re
def move(list1, list2, index):
    list2.append(list1[index])
    del list1[index]

def Stats(url, pitcher = True): #Downloads info from baseball website
    url = u.urlopen(url)
    content = url.read()#Gets HTML page
    content = content[1000:len(content)-20000]#Save time, butoff unneeded HTML
    end = content.index('batting_standard.2014')#Row with batting display 2014 (current when I made it)
    content1 = content[end:]#Narrows search more, don't need anything else before it
    times = re.findall(' >.*</td>', content1)#Finds each block in the row
    times = times[:18]#Don't need last 18 stats
    for i in times:
        times[times.index(i)] = i[2:len(i)-5]#Get's rid of surrounding tag
        
    del times[0]#MORE UNNECESARRY stats
    del times[1]#Highly tested and specific numbers
    del times[1]#Not generalied at all
    del times[0]#Don't use this code
    del times[1]#Probably doesn't even work on the website anymore
    del times[1]#This is so ugly but it worked
    del times[2]#Don't judge me
    if pitcher:#Pitcher stats
        other = content.index('pitching_standard.2014')#Row of content
        content2 = content[other:] #Cut off everything before it
        pitch= re.findall(' >.*</td>', content2)#All stats
        pitch = pitch[4:28]#Narrows search stats
        for i in pitch:
            pitch[pitch.index(i)] = i[2:len(i)-5]#Gets rid of the tag
        del pitch[-2]#all deletes unnecessary
        for i in range(5, 9): #Like I said, REALLY ugly
            del pitch[5]
        del pitch[0]
        del pitch[0]
        del pitch[7]
        del pitch[7]
        del pitch[7]
        print pitch
        pitch[1] = pitch[1][127:131]#Special case, true for all pitcher
        pitch[0] = "0"+pitch[0]#Adds decimal so we can convert to float
        del pitch[-2]
        del pitch[-2]#Rest of the not needed terms
        del pitch[-2]
        del pitch[-2]
        del pitch[-2]
        del pitch[2]
        del pitch[3]
        del pitch[4]
        for i in pitch:
            if '.' in i:#Checks for decimal so we don't convert to int()
                pitch[pitch.index(i)] = float(i)
                continue
            pitch[pitch.index(i)] = int(i)
        newPitch = []
        move(pitch, newPitch, 2)#Moves to new list
        move(pitch, newPitch, 1)#Puts in order for class
        move(pitch, newPitch, -2)
        move(pitch, newPitch, -2)
        move(pitch, newPitch, -1)
        move(pitch, newPitch, 0)
        print newPitch
        #Not needed anymore
    '''if hitter:
        newTimes = []
        move(times, newTimes, -1)#Takes the numbers from one list to another
        move(times, newTimes, 1)#And puts them in order of the class
        move(times, newTimes, 4)
        move(times, newTimes, -1)
        move(times, newTimes, -1)
        move(times, newTimes, 4)
        move(times, newTimes, 4)
        move(times, newTimes, 1)
        move(times, newTimes, 1)
        move(times, newTimes, 1)
        move(times, newTimes, 0)
        for i in newTimes:
            if '.' in i:
                newTimes[newTimes.index(i)] = float("0"+i)
                continue
            if newTimes.index(i) == len(newTimes)-1:
                newTimes[newTimes.index(i)] = float(i+".0")
                continue
            newTimes[newTimes.index(i)] = int(i)
        print newTimes'''
        
class Starter:
    #Starting pitcher, say, for the Cardinals
    def __init__(self, innings, era, strike, ball, whip, win, name, batting, runs, rbis, strikeB, ballB, stolen, caught, doubles, triples, home, game):
        self.innings = innings
        self.era = era
        self.strike = strike
        self.ball = ball
        self.whip = whip
        self.win = win
        self.game = game
        self.name = name
        self.batting = batting
        self.runs = runs
        self.rbis = rbis
        self.strikBe = strikeB
        self.ballB = ballB
        self.stolen = stolen
        self.caught = caught
        self.doubles = doubles
        self.triples = triples
        self.home = home
        self.game = game*4.25
        self.defense = 0.95       
        
class Reliever:
    #Relieves starting pitcher
    def __init__(self, name, era, strike, ball, whip, game):
        self.game = game*4.25        
        self.era = era
        self.strike = strike
        self.ball = ball
        self.whip = whip
        self.name = name
        self.defense = 0.95
        
class Player:
    #!pitcher (not a pitcher)
    def __init__(self, name, batting, runs, rbis, strike, ball, stolen, caught, doubles, triples, home, game):
        self.game = game*4.25        
        self.name = name
        self.batting = batting
        self.runs = runs
        self.rbis = rbis
        self.strike = strike
        self.ball = ball
        self.stolen = stolen
        self.caught = caught
        self.doubles = doubles
        self.triples = triples
        self.home = home
        self.defense = 0.95

#PLAYER()S NOT PITCHER()S OF VARIOUS TYPES    
AJP = Player("A.J. Pierzynski", 0.261, 19, 32, 41, 9, 0, 0, 11, 1, 4, 74.0)
TonyC = Player("Tony Cruz", 0.220, 4, 11, 18, 9, 0, 0, 4, 0, 0, 31.0)
KoltenW = Player("Kolten Wong", 0.250, 26, 24, 32, 13, 14, 2, 8, 2, 6, 61.0)
JhonnyP = Player("Jhonny Peralta", 0.254, 37, 44, 72, 38, 2, 2, 26, 0, 14, 101.0)
MarkE = Player("Mark Ellis", 0.185, 14, 12, 32, 13, 4, 1, 6, 0, 0, 60.0)
DanielD = Player("Daniel Descalso", 0.176, 7, 5, 22, 5, 1, 1, 5, 0, 0, 60.0)
MattC = Player("Matt Carpenter", 0.284, 67, 37, 78, 56, 3, 1, 23, 1, 6, 103.0)
MattA = Player("Matt Adams", 0.316, 34, 47, 69, 9, 3, 2, 23, 4, 12, 89.0)
JonJ = Player("Jon Jay", 0.289, 28, 24, 44, 14, 6, 1, 13, 2, 1, 91.0)
MattH = Player("Matt Holliday", 0.269, 57, 53, 70, 51, 2, 1, 25, 0, 10, 101.0)
AllenC = Player("Allen Craig", 0.24, 34, 44, 75, 25, 1, 1, 17, 1, 7, 95.0)
PeterB = Player("Peter Bourjos", 0.227, 19, 13, 55, 14, 8, 2, 6, 4, 3, 74.0)
#Starters (4 of them)
AdamW = Starter("Adam Wainwright", 149.2, 1.92, 122, 34, 0.962, 0.722, 0.217, 4, 3, 13, 3, 0, 0, 3, 0, 0, 21.0)
ShelbyM = Starter("Shelby Miller", 115.2, 4.2, 76, 55, 1.435, 0.467, 0.156, 3, 2, 18, 1, 0, 0, 4, 0, 0, 21.0)
LanceL = Starter("Lance Lynn", 127.0, 3.05, 117, 49, 1.315, 0.611, 0.027, 3, 1, 22, 3, 0, 0, 1, 0, 0, 21.0)
JoeK = Starter("Joe Kelly", 30.0, 3.9, 20, 15, 1.433, 0.667, 0.167, 0, 0, 1, 0, 0, 0, 1, 0, 0, 6.0)
#Relievers, whatever's left
KevinS = Reliever("Kevin Siegrit", 4.03, 59, 8, 1.209, 25)
TrevorR = Reliever("Trevor Rosenthal", 3.33, 62, 3, 1.356, 48)
PatN = Reliever("Pat Neshek", 0.85, 42, 6, 0.638, 47)
JasonM = Reliever("Jason Motte", 5.14, 15, 6, 1.476, 23)
CarlosM = Reliever("Carlos Martines", 4.58, 62, 30, 1.463, 37)
SethM = Reliever("Seth Maness", 2.7, 36, 8, 1.181, 46)
SamF = Reliever("Sam Freeman", 2.11, 20, 10, 1.219, 24)
RandyC = Reliever("Randy Choate", 4.56, 22, 8, 1.052, 41)