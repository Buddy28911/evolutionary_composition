# main.py
# By Danny Noe
# Evolutionary Composition
# main.py is responsible for initializing the program, as well as handling the command-line arguments

import argparse
from representation import representation, available_outports
from gen_alg import algorithm_args, run_genetic_algorithm

key_sig = ["Cb","Gb","Db","Ab","Eb","Bb","F","C","G","D","A","E","B","F#","C#"]
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outport', type=str, help="Sets the outport device for MIDO. If none is given, you will get the (system specific) default port.")
parser.add_argument('-v', '--verbosity', action='store_true', help="Outputs program's settings")
parser.add_argument('-k', '--key_signature', type=str, help="Sets the key signature for the program", choices=key_sig, default="C")
parser.add_argument('-t', '--tempo', type=int, help="Sets the tempo (in BPM) for the program", choices=range(1, 301), metavar="[0,300]", default=120)

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser.add_argument('-b', '--back_track', type=str2bool, nargs='?', help="Enables a backing track. Turn on the track with True, False for off.", default=True)
parser.add_argument('-a', '--arp_or_scale', type=str2bool, nargs='?', help="Sets the backing track to play an ascending arpeggio or scale. True for arp, false for scale", default=True)


# Algorithms
gen_alg = parser.add_argument_group('Genetic Algorithms', 'Choose from several different genetic algorithms: eaSimple, eaMuPlusLambda, eaMuCommaLambda')
gen_alg.add_argument('-ga', '--genetic_alg', type=str, 
                    help="Sets the genetic algorithm to use. eaMuPlusLambda: (𝜇 + 𝜆) evolutionary algorithm | eaMuCommaLambda: (𝜇 , 𝜆) evolutionary algorithm |  eaSimple: the simplest evolutionary algorithm", 
                    choices=['eaMuPlusLambda', 'eaMuCommaLambda', 'eaSimple'], default='eaMuPlusLambda')

# Algorithm options
gen_al_args = parser.add_argument_group('Genetic Algorithm Arguments', 
                    'eaMuPlusLambda arguments: mu, lambda_, cxpb, mutpb, ngen | eaMuCommaLambda arguments: mu, lambda_, cxpb, mutpb, ngen | eaSimple arguments: cxpb, mutpb, ngen')

gen_al_args.add_argument('--popsize', type=int, help="Sets the number of melodies to generate in the initial population.", default=6)
gen_al_args.add_argument('--ngen', type=int, help="ngen sets the number of generations the GA will run for.", default=6)
gen_al_args.add_argument('--mu', type=int, help="mu sets the number of individuals to select for the next generation.", default=3)
gen_al_args.add_argument('--lambda_', type=int, help="lambda_ sets number of children to produce at each generation.", default=10)
gen_al_args.add_argument('--cxpb', type=float, help="cxpb sets the probability that an offspring is produced by crossover.", metavar="[0,1)", default=0.7)
gen_al_args.add_argument('--mutpb', type=float, help="mutb sets the probability that an offspring is produced by mutation.", metavar="[0,1)", default=0.3)

def main():
    print("Welcome to the evolutionary composition program!")
    args = parser.parse_args()
    if args.verbosity:
        print("Available outports:", available_outports())
        print("Selected key is", args.key_signature)
        print("The tempo is", args.tempo)
        if args.back_track:
            print("The backing track is on.", end=" ")
            if args.arp_or_scale:
                print("Arpeggio selected.")
            else:
                print("Scale selected.")
        else:
            print("Backing track disabled.")
        
    rep_obj = representation(args.key_signature, args.tempo, args.back_track, args.arp_or_scale, args.outport)
    alg_args = algorithm_args(args.genetic_alg, args.popsize, args.ngen, args.mu, args.lambda_, args.cxpb, args.mutpb)
    population, hall_of_fame = run_genetic_algorithm(rep_obj, alg_args)
    return population, hall_of_fame

if __name__ == "__main__":
    main()