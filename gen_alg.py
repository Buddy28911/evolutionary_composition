# Genetic Algorithm file
# By Danny Noe

import random

import numpy

from deap import algorithms, base, creator, tools

from representation import representation, save_best_melodies, Melody


class algorithm_args:
    """
    The algorithm_args object contains all of the algorithm arguments recieved on the command-line.
    algorithm_args simplifies number of arguments that need to be sent to run_program()
    """
    def __init__(self, algorithm: str, pop_size: int, ngen: int, mu: int, lambda_: int, cxpb: float, mutpb: float):
        """
        Initializes the algorithm_args object with arguments given on the command-line
        Input: algorithm: str, the name of the genetic algorithm | pop_size: int, the size of the initial population
        ngen: int, the number of generations the ga will run for | mu: int, the number of individuals to select for the next generation
        lambda_: int, sets number of children to produce at each generation | cxpb: float, the probability that an offspring is produced by crossover
        mutpb: float, the probability that an offspring is produced by mutation
        Output: algorithm_args object
        """
        self.algorithm = algorithm
        self.pop_size = pop_size
        self.ngen = ngen
        self.mu = mu
        self.lambda_ = lambda_
        self.cxpb = cxpb
        self.mutpb = mutpb
        return

def cx_music(input_mel1: Melody, input_mel2: Melody):
    """
    cx_music() performs a crossover operation on two given melodies
    Input: input_mel1: Melody, the first melody | input_mel2: Melody, the second melody
    Output: child1: Melody, [[First half of input_mel2's measures], [Second half of input_mel1's measures]] 
    child2, Melody: [[First half of input_mel1's measures], [Second half of input_mel2's measures]]
    """
    # Make temp copy
    mel_copy = input_mel1.copy()
    # Child 1
    input_mel1.cross_mel(input_mel2, True)

    # Child 2
    input_mel2.cross_mel(mel_copy, False)
    
    return input_mel1, input_mel2

def mut_melody(input_mel: Melody):
    """
    mut_melody() mutates a given melody. The function iterates over the whole melody
    performing a coin flip on each note determining if it should be pitch shifted up or down
    Input: input_mel: Melody, the melody to be mutated
    Output: input_mel: Melody, the mutated melody
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

def load_midi(population: list, toolbox, key: str):
    """
    The load_midi() function reads MIDI files entered by the user from the ./midi_out/ directory
    and adds them to the population
    Input: population: list, the current deap population list | toolbox: Toolbox, the current deap Toolbox
    key: str, the key signature the program is using
    Output: population: list, the updated population with read MIDIs added | pop_size: int, the updated size of the population
    """
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
    """
    The run_genetic_algorithm is the main method of the evolutionary composition project.
    The method takes in all arguments, then runs the selected genetic algorithm.
    After ngens, the best MIDIs are written to the ./midi_out/ directory
    Input: rep_obj: representation, contains the necessary representation arguments
    alg_args: algorithm_args, contains the necessary genetic algorithm arguments
    Output: population: list, a deap population containing the last generation of melodies
    hall_of_fame: deap.tools.support.ParetoFront, deap hall_of_fame object containing melodies the user rated 5/5
    """

    # Fitness func has one weight, maximizing good melodies
    creator.create("FitnessMax", base.Fitness, weights=(1.0, )) # weights must be tuples, but we only have parameter to maximize
    creator.create("Melody", Melody, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    # Melody class has to registered to the deap toolbox
    toolbox.register("melody", creator.Melody, key=rep_obj.key_signature) # the key signature must be passed to generate a melody
    toolbox.register("population", tools.initRepeat, list, toolbox.melody)

    toolbox.register("mate", cx_music)
    toolbox.register("mutate", mut_melody)
    toolbox.register("select", tools.selNSGA2)
    toolbox.register("evaluate", representation.evaluate_music, rep_obj)
    
    population = toolbox.population(n=alg_args.pop_size)

    num = 0
    for melody in population:
        filename = "midi_for_steve" + str(num) + ".mid"
        rep_obj.melody_to_midi(melody, filename, False)
        num += 1
    
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