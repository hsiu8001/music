import csv
import numpy as np
from music21 import*
import random
import re

count = 0
with open('sheet.csv','rt') as fileX:
    filereader = csv.reader(fileX)
    mydict = {}
    for i in filereader:
        for k in i:
            if(k!=''):
                count+=1
                #print(k)
                if k in mydict:
                    mydict[k] +=1
                else :
                    mydict[k] = 1
    #print('count = ',count)
    for j in mydict:
        mydict[j] = mydict[j]/count
    #print(mydict)
    chords = mydict.keys()
    chords = list(chords)
    
    probability = mydict.values() 
    probability = list(probability)
    #print(chords)
    #print(probability)    

    song = []
    song = np.random.choice(chords, size=16, replace = True, p = probability )
    #print(song)
    
music = stream.Stream()
for c in song:
    if '-' in c:
        c = c.replace('-', 'b')
    elif 'b' in c:
        c = c.replace('b', '-')
    har = harmony.ChordSymbol(c)
    music.append(har)
    notes = [str(p) for p in har.pitches]
    for i in range(0, 4):
        ran = random.randrange(0, len(notes))
        r = re.search(r'\d', notes[ran])
        a = r.group()
        tmp = notes[ran].replace(a, chr(ord(a)+1))
        music.append(note.Note(tmp))
    #music.repeatAppend(note.Rest(), 4)
    #print(c, har)
music.show()