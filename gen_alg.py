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

from Representation import Melody

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
    """
    return

def mut_music(input_mel):
    """
    Mutation function for music that mutates a give melody: input_mel
    """
    return

test_mel = Melody()
print(test_mel)
print(test_mel.len())

# Fitness func has one weight, maximizing good melodies
creator.create("FitnessMax", base.Fitness, weights=(1.0, )) # weights must be tuples, our fitnessmax function maximizes
creator.create("Melody", Melody, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("population", tools.initRepeat, list, creator.Melody)

the_populatation = toolbox.population(n=POP_SIZE)
print(the_populatation)

i = 0
for mel in the_populatation:
    #print("Melody " + str(i) + " " + str(mel))
    i+=1

for mel in the_populatation:
    print(evaluate_music(mel))