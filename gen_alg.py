# Genetic Algorithm file
# By Danny Noe

import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

from representation import Melody
from representation import play

POP_SIZE = 6    # Dictates the number of melodies in a population

def evaluate_music(input_mel):
    """
    Evaluation function for music that evaluates a given melody
    """
    play(input_mel) # Need function to play each melody for user
    usr_rating = input("Did you enjoy that little diddy? Please rate from 0-5 (ints only) ")
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

def mut_music(input_mel: Melody):
    """
    Mutation function for music that mutates a given melody: input_mel
    Mutates a melody by 
    Returns a mutated version of the given melody
    """
    for measure in input_mel.melody_list:
        for note in measure.measure_list:
            if random.random() < 0.5 and note.note_pitch != 84:
                note.pitch_shift()
            elif note.note_pitch != 60:
                note.pitch_shift(up=False)
            else:
                return
    return input_mel, 

# Fitness func has one weight, maximizing good melodies
creator.create("FitnessMax", base.Fitness, weights=(1.0, )) # weights must be tuples, our fitnessmax function maximizes
creator.create("Melody", Melody, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("population", tools.initRepeat, list, creator.Melody)
toolbox.register("evaluate", evaluate_music)
toolbox.register("mate", cx_music)
toolbox.register("mutate", mut_music)
toolbox.register("select", tools.selNSGA2)

def main():
    print("Begining")
    NGEN = 10   # Num generations
    MU = 2      # Num of individuals to select for next generation
    LAMBDA = 6  # The number of children to produce at each generation
    CXPB = 0.7  # Probability than an offspring is produced by crossover
    MUTPB = 0.2 # Probability that an offspring is produced by mutation
    
    population = toolbox.population(n=POP_SIZE)
    hall_of_fame = tools.ParetoFront()

    # Stats
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    algorithms.eaMuPlusLambda(population, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats, hall_of_fame)

    return population, stats, hall_of_fame


if __name__ == "__main__":
    main()


"""
Backup/test code things:

the_populatation = toolbox.population(n=POP_SIZE)
print(the_populatation)
i = 0
for mel in the_populatation:
    print("Playing melody:", i)
    i+=1
    tup = evaluate_music(mel)
    print(tup)

test_mel = Melody()
print(test_mel)
print(test_mel.len())

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
print(mel1)
mut_music(mel1)
print(mel1)
"""