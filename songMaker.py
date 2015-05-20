# -*- coding: utf-8 -*-
"""
Allows the user to play songs from this http://resistorsings.com/106/
"""

from interact import typeLettersTime, typeLetterTime
import time as t
import sys
songs = []
strings = []
def openFile():
    lisst = open('songs.txt', 'r')
    for i in lisst:
        i = i.strip()
        if i != "BLANK" and i[0] not in "1234567890":
            songs.append(i.lower())
        else:
            if i != 'BLANK':
                strings.append(i)
    lisst.close()

def saveSong():
    appended = ""
    f = open('songs.txt', 'a')
    name = raw_input("Please type in song name (no numbers please) \n> ")
    appended += name
    appended += "\n"
    appended += x
    appended += "\n"
    appended += "BLANK"
    appended += "\n"
    f.write(appended)
    
def deleteSong():
    x = 0
    f = open('songs.txt', 'r')
    name = raw_input("What song would you like to delete?\n> ")
    if name not in songs:
        print "Song not found"
        sys.exit(0)
    else:
        lines = f.readlines()
    f.close()
    f = open('songs.txt', 'w')
    for line in lines:
        if x > 0:
            x -= 1
            continue
        elif line.strip().lower() == name:
             x = 4
             x -= 1
             continue
        else:
            f.write(line)
    
openFile()
width = len(max(songs))
print "The following program will allow you to play songs"
print "To play chords, type the letters together with no spaces"
print "To delay a chord/note for a specific amount of time, "
print "Type a number immediately following the note/chord"
print "(no spaces) signifying how many sixteenth notes the note"
print "Use the tilda (~) to signify rest, using the same time thing"
print "-----------"
print "To begin, type del playback or write to do one of those things"
print "Names of songs saved:"
for pos, name in enumerate(songs):
    print str(pos+1) + "." + " %s" % (name.rjust(width))

playback = raw_input("Type del, play, or write\n> ")
if playback.lower() == 'play':
    name = raw_input("Type song name \n> ")
    if name.lower() not in songs:
        print "Error, song not found"
        sys.exit(0)
    else:
        x = strings[songs.index(name)]
elif playback.lower() == 'write':
    print "Please make sure your song starts out with the tempo"
    x = raw_input("Type in your sequence\n> ")
else:
    deleteSong()
    sys.exit(0)

t.sleep(3)

notes = x.split() #returns list of all the notes
tempo = notes[0]
notes = notes[1:]
tempo = 0.25*(60.0/float(tempo))
for i in notes: #Iterating through the notes
    if len(i) > 2: #It's a chord (note+length)
        typeLettersTime(list(i)[:-1], tempo*float(i[-1]))#Notes are all but the last one
    elif i[0] == '~':
        t.sleep(tempo*float(i[-1]))
    else:
        typeLetterTime(i[0], tempo*float(i[1]))
if playback == 'write':
    print "Would you like to save your song?"
    save = raw_input("(y/n)\n ")
    if save == 'y':
        saveSong()
        