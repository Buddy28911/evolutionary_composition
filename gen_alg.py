# Genetic Algorithm file
# By Danny Noe

import random

import numpy

from deap import algorithms, base, creator, tools

from representation import representation, save_best_melodies, Melody


class algorithm_args:
    def __init__(self, algorithm, pop_size, ngen, mu, lambda_, cxpb, mutpb):
        self.algorithm = algorithm
        self.pop_size = pop_size
        self.ngen = ngen
        self.mu = mu
        self.lambda_ = lambda_
        self.cxpb = cxpb
        self.mutpb = mutpb
        return

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
    #print("After ", str(input_mel2))
    return input_mel1, input_mel2

def mut_music(input_mel):
    """
    Mutation function for music that mutates a given melody: input_mel
    Mutates a melody by 
    Returns a mutated version of the given melody
    """
    for measure in input_mel.melody_list:
        for note in measure.measure_list:
            if random.random() < 0.5:
                if note.note_pitch != 84 and note.note_pitch != 128:
                    note.pitch_shift()
            else:
                if note.note_pitch != 60 and note.note_pitch != 128:
                    note.pitch_shift(up=False)

    return input_mel, 

def load_midi(population, toolbox, key):
    print("MIDI files saved to ./midi_out/ can be added to the population.")
    print("Note: MIDIs written by this program in previous sessions work best.")
    print("Note: Do not include the folder path.")
    print("Note: The pop_size arg will be updated to include read files.")
    more_input = True
    while more_input:
        # Handle the user's input
        filename = input("Enter a MIDI file? (No to stop) ")
        if filename.lower() == "no" or filename.lower() == "n":
            more_input = False
            break
        else:
            try:
                new_pop_item = toolbox.melody(filename=filename)
                population.append(new_pop_item)
            except FileNotFoundError:
                print("Error: File not found")
            
    return len(population)

def run_genetic_algorithm(rep_obj, alg_args):

    # Fitness func has one weight, maximizing good melodies
    creator.create("FitnessMax", base.Fitness, weights=(1.0, )) # weights must be tuples, our fitnessmax function maximizes
    creator.create("Melody", Melody, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("melody", creator.Melody, key=rep_obj.key_signature)
    toolbox.register("population", tools.initRepeat, list, toolbox.melody)

    toolbox.register("mate", cx_music)
    toolbox.register("mutate", mut_music)
    toolbox.register("select", tools.selNSGA2)
    toolbox.register("evaluate", representation.evaluate_music, rep_obj)
    
    population = toolbox.population(n=alg_args.pop_size)
    
    alg_args.pop_size = load_midi(population, toolbox, rep_obj.key_signature)

    hall_of_fame = tools.ParetoFront()

    if alg_args.algorithm == "eaMuCommaLambda":
        algorithms.eaMuCommaLambda(population, toolbox, alg_args.mu, alg_args.lambda_, alg_args.cxpb, alg_args.mutpb, alg_args.ngen, None, hall_of_fame)
    elif alg_args.algorithm == "eaMuPlusLambda":
        algorithms.eaMuPlusLambda(population, toolbox, alg_args.mu, alg_args.lambda_, alg_args.cxpb, alg_args.mutpb, alg_args.ngen, None, hall_of_fame)
    elif alg_args.algorithm == "eaSimple":
        algorithms.eaSimple(population, toolbox, alg_args.cxpb, alg_args.mutpb, alg_args.ngen, None, hall_of_fame)
    
    save_best_melodies(rep_obj, population, hall_of_fame)
    return population, hall_of_fame

