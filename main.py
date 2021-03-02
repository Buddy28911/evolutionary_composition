# Main file for Danny Noe's Evolutionary Music Project

import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

import ctcsound

from Representation import Melody

from gen_alg import test_me

test_mel = Melody()
print(test_mel)
print(test_mel.len())

# Fitness func has one weight, maximizing good melodies
creator.create("FitnessMax", base.Fitness, weights=(1.0, )) # weights must be tuples, our fitnessmax function maximizes
creator.create("Melody", Melody, fitness=creator.FitnessMax)

test_me()