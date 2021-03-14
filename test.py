# Makes a function that will contain the
# desired program.
def example():

    # Calls for an infinite loop that keeps executing
    # until an exception occurs
    while True:
        test4word = input("What's your name? ")

        try:
            test4num = int(input("From 1 to 7, how many hours do you play in your mobile?" ))

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")

        # When successfully converted to an integer,
        # the loop will end.
        else:
            print("Impressive, ", test4word, "! You spent", test4num*60, "minutes or", test4num*60*60, "seconds in your mobile!")
            break

# The function is called
#example()

from representation import Melody
from representation import play
from representation import melody_to_midi

def evaluate_music(input_mel):
    """
    Evaluation function for music that evaluates a given melody
    """
    print("Playing Melody ...")
    play(input_mel) # Need function to play each melody for user
    
    while True:
        # Handle the user's input
        usr_string = input("Did you enjoy that little diddy? Please rate from 0-5 (ints only). To hear it again type replay: ")
        if usr_string.lower() == "replay":
            print("Playing Melody ...")
            play(input_mel)
        elif usr_string.lower() == "save":
            melody_to_midi(input_mel, "program_melody.mid", 80)
        else:
            try:
                usr_rating = int(usr_string)
            except ValueError:
                print("Error: Invalid input. Please rate the melody from 0-5 or enter replay to hear it again: ")
            else:
                if usr_rating < 0 or usr_rating > 5:
                    print("Error: Rating out of bounds. Please rate the melody from 0-5")
                else:
                    break

    return usr_rating,

#melody = Melody()
#ret_tup = evaluate_music(melody)
#print(ret_tup)
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo, second2tick

outport = mido.open_output(None)
#melody = Melody()
#print(melody)
#melody_to_midi(melody, './Project/Code/new_mid.mid', 164)
mid_file = MidiFile('/Users/dannynoe/Documents/URI/CSC 499/Project/Code/midi_out/program_melody.mid')

# for message in mid_file.play():
#     print(message)
#     outport.send(message)

print(mid_file.length)
s2t = second2tick(mid_file.length)
print(s2t)


print("Done.")