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
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo, second2tick, tempo2bpm
from representation import Note, MIDI_TO_NOTE

outport = mido.open_output(None)
melody = Melody()
#play(melody)
#print(melody)
original_str = str(melody)
melody_to_midi(melody, 'program_melody2.mid', 100)
mid_file = MidiFile('/Users/dannynoe/Documents/URI/CSC 499/Project/Code/midi_out/program_melody2.mid')


tempo = 0
key_signature = ""
for message in mid_file.play(True):
    print(message)
    if message.is_meta:
        print("meta")
        if message.type == 'key_signature':
            key_signature = message.key
        elif message.type == 'set_tempo':
            tempo = message.tempo
    else:
        break
        #outport.send(message)


# Convert MIDI time to micro-seconds 60000 / (BPM * PPQ) PPQ = ticks_per_beat

print(mid_file.length)
print(mid_file.ticks_per_beat)
ticks_per_beat = mid_file.ticks_per_beat
tempo = int(tempo2bpm(tempo) + 0.5)
print(tempo)
seconds_per_tick =  (60000 / (tempo * ticks_per_beat)) / 1000000
print(seconds_per_tick)
note_list = []
rest = False
sum_beats = 0.0
for message in mid_file:
    print(message)
    if message.is_meta:
        print("meta")
        pass
    else:
        print("Note")
        if message.time != 0:
            if rest:
                pass
                n_p = "Rest"
                rest = False
            else:
                n_p = message.note
            vel = message.velocity
            time = message.time
            ticks = time / seconds_per_tick
            beats = ticks / ticks_per_beat
            beats = beats / 1000
            beats = round(beats, 2)
            sum_beats += beats
            note_list.append(Note(n_p, beats, vel))
        elif message.type == 'note_off':
            rest = True
        else:
            pass

read_str = ""        
for note in note_list:
    read_str += str(note)
    print(note)

print("Original melody")
print(original_str)
print("Read string")
print(read_str)

print(sum_beats)
print("Done.")