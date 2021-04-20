# Main file for Danny Noe's Evolutionary Music Project

#from music_data import *
import argparse
from representation import representation
from gen_alg import run_eaMuPlusLambda
from gen_alg import run_eaMuCommaLambda
from gen_alg import algorithm_args

key_sig = ["Cb","Gb","Db","Ab","Eb","Bb","F","C","G","D","A","E","B","F#","C#"]
parser = argparse.ArgumentParser()
#parser.add_argument('-o', '--output', action='store_true', help="shows output")
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
# Todo: Add descending option?
#parser.add_argument('-m', '--measures_p_melody', type=int, help="Sets the number of measures per each melody")

# Algorithms
gen_alg_group = parser.add_mutually_exclusive_group()
gen_alg_group.add_argument('--eaMuPlusLambda', action='store_true', help="Use the (𝜇 + 𝜆) evolutionary algorithm.")
gen_alg_group.add_argument('--eaMuCommaLambda', action='store_true', help="Use the (𝜇 , 𝜆) evolutionary algorithm.")
# Algorithm options
gen_al_args = parser.add_argument_group('Genetic Algorithm Arguments', 'eaMuPlusLambda arguments: mu, lambda_, cxpb, mutpb, ngen\neaMuCommaLambda arguments: mu, lambda_, cxpb, mutpb, ngen')
gen_al_args.add_argument('--popsize', type=int, help="Sets the number of melodies to generate in a generation.", default=6)
gen_al_args.add_argument('--ngen', type=int, help="ngen sets the number of generations", default=6)
gen_al_args.add_argument('--mu', type=int, help="mu sets the numer of individuals to select for the next generation", default=3)
gen_al_args.add_argument('--lambda_', type=int, help="lambda_ sets number of children to produce at each generation.", default=6)
gen_al_args.add_argument('--cxpb', type=float, help="cxpb sets the probability that an offspring is produced by crossover", metavar="[0,1)", default=0.7)
gen_al_args.add_argument('--mutpb', type=float, help="mutb sets the probability that an offspring is produced by mutation", metavar="[0,1)", default=0.3)

def main():
    print("Welcome to the evolutionary composition program!")
    args = parser.parse_args()
    if args.verbosity:
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
        
    rep_obj = representation(args.key_signature, args.tempo, args.back_track, args.arp_or_scale, None)
    alg_args = algorithm_args(args.popsize, args.ngen, args.mu, args.lambda_, args.cxpb, args.mutpb)
    if args.eaMuPlusLambda:
        population, hall_of_fame = run_eaMuPlusLambda(rep_obj, alg_args)
    elif args.eaMuCommaLambda:
        population, hall_of_fame = run_eaMuCommaLambda(rep_obj, alg_args)

if __name__ == "__main__":
    main()