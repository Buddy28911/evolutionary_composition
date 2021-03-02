#Testing and saving code here
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

import ctcsound

# Fitness func has one weight, maximizing good melodies
creator.create("Fitness", base.Fitness, weights=(1.0, ))
#creator.create("Measure", list,  )

def greeting(name: str) -> str:
    return 'Hello ' + name

joe = greeting("Joe")
print(joe)

def Note(note_pitch: float, start: int, end: int) -> list:
    return [note_pitch, start, end]

note_C = Note(8.00, 0, 1)
print(note_C)

orc = """
sr=44100
ksmps=32
nchnls=2
0dbfs=1

instr 1
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4 * kenv, ipch
aout moogladder aout, 2000, 0.25
outs aout, aout
endin"""

sco = ""
sco += "i1 " + str(note_C[1]) + " " + str(note_C[2]) + " " + "0.5" + " " + str(note_C[0]) + "\n"



#sco += "i1 0 1 0.5 8.00"
print(sco)


c = ctcsound.Csound()
c.setOption("-odac")

c.compileOrc(orc)   # Compile the Csound Orchestra string
c.readScore(sco)    # Compile the Csound SCO String
c.start()           # When compiling from strings, this call is necessary before doing any performing
c.perform()         # Run Csound to completion
c.reset()

scale = []
time = 0
for i in range(13):
    scale += [Note(8.00 + (0.01 * i), time, time+1)]
    time += 2
print(scale)

sco = ""
for note in scale:
    sco += "i1 " + str(note[1]) + " " + str(note[2]) + " " + "0.5" + " " + str(note[0]) + "\n"

#c = ctcsound.Csound()
c.setOption("-odac")

c.compileOrc(orc)   # Compile the Csound Orchestra string
c.readScore(sco)    # Compile the Csound SCO String
c.start()           # When compiling from strings, this call is necessary before doing any performing
c.perform()         # Run Csound to completion
c.reset()

print(sco)