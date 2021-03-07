def test_me():
    print("Hello World!")
# Genetic Algorithm file
# By Danny Noe

import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

import ctcsound

from representation import Melody
from representation import NOTE_RANGE
POP_SIZE = 6    # Dictates the number of melodies in a population

def evaluate_music(input_mel):
    """
    Evaluation function for music that evaluates a given melody
    """
    print(str(input_mel))
    #play(melody) # Need function to play each melody for user
    usr_rating = input("Did you enjoy that little diddy? Please rate from 1-5 (ints only) ")
    return int(usr_rating),

def cx_music(input_mel1, input_mel2):
    """
    Crossover function for music that performs a crossover operation on two given melodies: input_mel1, input_mel2
    Returns two children child1, child2
    Child1: [[First half of input_mel2's measures], [Second half of input_mel1's measures]]
    Child2: [[First half of input_mel1's measures], [Second half of input_mel2's measures]]
    """
    # Make temp copy
    mel_copy = input_mel1.copy()
    # Child 1
    #print("Child 1 Before ", str(input_mel1))
    input_mel1.cross_mel(input_mel2, True)
    #print("After ", str(input_mel1))
    # Child 2
    #print("Child 2 Before ", str(input_mel2))
    input_mel2.cross_mel(mel_copy, False)
    print("After ", str(input_mel2))
    return input_mel1, input_mel2

def mut_music(input_mel):
    """
    Mutation function for music that mutates a given melody: input_mel
    Mutates a melody by 
    Returns a mutated version of the given melody
    """
    for measure in input_mel:
        for note in measure:
            if note.note_pitch == "Rest" and note.beats == 4.0:
                note.note_pitch = random.choice(NOTE_RANGE)
                # Reassigns the pitch of a whole rest to a whole note
                # Note: may want to remove whole notes for short melodies entirely
            elif random.random() < 0.5:
                
    return input_mel, 

# Fitness func has one weight, maximizing good melodies
creator.create("FitnessMax", base.Fitness, weights=(1.0, )) # weights must be tuples, our fitnessmax function maximizes
creator.create("Melody", Melody, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("population", tools.initRepeat, list, creator.Melody)

test_mel = Melody()
print(test_mel)
print(test_mel.len())

the_populatation = toolbox.population(n=POP_SIZE)
print(the_populatation)

i = 0
for mel in the_populatation:
    #print("Melody " + str(i) + " " + str(mel))
    i+=1

#for mel in the_populatation:
    #print(evaluate_music(mel))

copy_of = test_mel.copy()
print("test:", str(test_mel))

print("copy", str(copy_of))
mel1 = Melody()
mel2 = Melody()
cx_music(mel1, mel2)