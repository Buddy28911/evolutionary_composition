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

test_mel = Melody()
print(test_mel)
print(test_mel.len())

# Fitness func has one weight, maximizing good melodies
creator.create("FitnessMax", base.Fitness, weights=(1.0, )) # weights must be tuples, our fitnessmax function maximizes
creator.create("Melody", Melody, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("population", tools.initRepeat, list, creator.Melody)

the_populatation = toolbox.population(n=2)
print(the_populatation)

i = 0
for mel in the_populatation:
    print("Melody " + str(i) + str(mel))
    i+=1