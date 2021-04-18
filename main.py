# Main file for Danny Noe's Evolutionary Music Project

#from music_data import *
import argparse
from representation import representation
from gen_alg import run_program

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
    
    run_program(rep_obj)

if __name__ == "__main__":
    main()