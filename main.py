# Main file for Danny Noe's Evolutionary Music Project

import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

import ctcsound

from Representation import Note
from Representation import Measure

test_note_1 = Note("C4", 1.0)
print(test_note_1)
test_note_2 = Note("Rest", 2.0)
print(test_note_2)
rand_note = Note()
print(rand_note)
print(rand_note.note_pitch)

FirstM = Measure()
print("Notes in list:")
for m_note in FirstM.measure_list:
    print(m_note)

print(FirstM)
# Fitness func has one weight, maximizing good melodies
creator.create("Fitness", base.Fitness, weights=(1.0, ))
#creator.create("Measure", tools.initRepeat, list, )


