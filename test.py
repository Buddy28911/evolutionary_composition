# Testing Reading / Writing MIDI files
from representation import *
from music_data import *

def midi_test_mel_fun():
    measure_1 = []
    for i in range(2):
        measure_1.append(Note("D5", 2.0, 80))
        #midi_melody_list.append(Note("D5", 2.0, 80))

    measure_2 = []
    for i in range(4):
        measure_2.append(Note("E5", 1.0, 80))

    measure_3 = []
    for i in range(8):
        measure_3.append(Note("G5", 0.5, 80))

    measure_4 = []
    for i in range(16):
        measure_4.append(Note("A5", 0.25, 80))

    meas_1 = Measure(measure_1)
    meas_2 = Measure(measure_2)
    meas_3 = Measure(measure_3)
    meas_4 = Measure(measure_4)
    midi_melody_list =  meas_1, meas_2, meas_3, meas_4
    midi_melody = Melody(melody_list=midi_melody_list)
    #print(midi_melody)
    return midi_melody

def midi_test_mel_fun_with_rest():
    measure_1 = []
    for i in range(2):
        if i % 2 != 0:
            measure_1.append(Note("D5", 2.0, 80))
        else:
            measure_1.append(Note("Rest", 2.0, 80))
        #midi_melody_list.append(Note("D5", 2.0, 80))

    measure_2 = []
    for i in range(4):
        if i % 2 != 0:
            measure_2.append(Note("E5", 1.0, 80))
        else:
            measure_2.append(Note("Rest", 1.0, 80))

    measure_3 = []
    for i in range(8):
        if i % 2 != 0:
            measure_3.append(Note("G5", 0.5, 80))
        else:
            measure_3.append(Note("Rest", 0.5, 80))

    measure_4 = []
    for i in range(16):
        if i % 2 != 0:
            measure_4.append(Note("A5", 0.25, 80))
        else:
            measure_4.append(Note("Rest", 0.25, 80))

    meas_1 = Measure(measure_1)
    meas_2 = Measure(measure_2)
    meas_3 = Measure(measure_3)
    meas_4 = Measure(measure_4)
    midi_melody_list =  meas_1, meas_2, meas_3, meas_4
    midi_melody = Melody(melody_list=midi_melody_list)
    #print(midi_melody)
    return midi_melody

def midi_to_melody(mid_file: MidiFile):
    tempo = 0
    key_signature = ""

    # Get the metadata
    for message in mid_file:
        if message.is_meta:
            if message.type == 'key_signature':
                key_signature = message.key
            elif message.type == 'set_tempo':
                tempo = message.tempo
        else:
            break
    
    # Read all the notes
    note_list = []
    rest = False
    melody_track = mid_file.tracks[0]
    new_note_list = [0, 0.0, 0] # Note, Beats, Velocity
    new_note = True

    for message in melody_track:
        if message.is_meta:
            pass
        elif MIDI_TO_NOTE[message.note] not in NOTE_RANGE:
            pass
        else:
            if new_note:
                new_note_list[0] = message.note
                new_note_list[2] = message.velocity
                new_note = False
            if message.time != 0:
                if rest:
                    new_note_list[0] = "Rest"
                    rest = False

                beat_val = message.time
                # beat_val = note.beats * ticks_per_beat
                ticks_per_beat = mid_file.ticks_per_beat
                beats = beat_val / ticks_per_beat
                
                new_note_list[1] = beats

                note_list.append(Note(new_note_list[0], new_note_list[1], new_note_list[2]))

                new_note = True
            elif message.type == 'note_off':
                rest = True

    #print(note_list)

    return build_melody(note_list)

def build_melody(note_list: list):
    measure_list = []
    measure_beats = 0.0
    sum_beats = 0.0
    melody_list = []

    max_beats = BEATS_P_MEASURE * MEASURES_P_MELODY * 1.0
    for note in note_list:
        measure_beats += note.beats
        sum_beats += note.beats
        measure_list.append(note)
        if measure_beats == BEATS_P_MEASURE:
            melody_list.append(Measure(measure_list))
            measure_beats = 0.0
            measure_list = []

    if sum_beats > max_beats:
        raise Exception("Error: Beats in MID exceed ", max_beats)
    else:
        return melody_list

# note = "C4"
# print(note[1])

# max_beats = BEATS_P_MEASURE * MEASURES_P_MELODY * 1.0
# print(type(max_beats))

# scale = ["B2", "C3#", "D3#", "E3", "F3#", "G3#", "A3#", "B3"]
# sca = []
# for note in scale:
#     num = int(note[1]) + 2
#     shifted_note = note[0] + str(num)
#     if len(note) == 3:
#         shifted_note += note[2]
#     sca.append(shifted_note)

# print(scale)
# print(sca)

# for key in SCALES:
#     shifted_scale = shift_scale(key)
#     if len(shifted_scale) != 8:
#         print(shifted_scale)


test = Melody("C")
print(test)
# test_mel = MidiFile("./midi_out/midi_melody_test.mid")
# read_list = midi_to_melody(test_mel)
# print(read_list)
#melody_2 = Melody()
#print(melody_2)
# # Makes a function that will contain the
# # desired program.
# def example():

#     # Calls for an infinite loop that keeps executing
#     # until an exception occurs
#     while True:
#         test4word = input("What's your name? ")

#         try:
#             test4num = int(input("From 1 to 7, how many hours do you play in your mobile?" ))

#         # If something else that is not the string
#         # version of a number is introduced, the
#         # ValueError exception will be called.
#         except ValueError:
#             # The cycle will go on until validation
#             print("Error! This is not a number. Try again.")

#         # When successfully converted to an integer,
#         # the loop will end.
#         else:
#             print("Impressive, ", test4word, "! You spent", test4num*60, "minutes or", test4num*60*60, "seconds in your mobile!")
#             break

# # The function is called
# #example()

# from representation import Melody
# from representation import play
# from representation import melody_to_midi

# def evaluate_music(input_mel):
#     """
#     Evaluation function for music that evaluates a given melody
#     """
#     print("Playing Melody ...")
#     play(input_mel) # Need function to play each melody for user
    
#     while True:
#         # Handle the user's input
#         usr_string = input("Did you enjoy that little diddy? Please rate from 0-5 (ints only). To hear it again type replay: ")
#         if usr_string.lower() == "replay":
#             print("Playing Melody ...")
#             play(input_mel)
#         elif usr_string.lower() == "save":
#             melody_to_midi(input_mel, "program_melody.mid", 80)
#         else:
#             try:
#                 usr_rating = int(usr_string)
#             except ValueError:
#                 print("Error: Invalid input. Please rate the melody from 0-5 or enter replay to hear it again: ")
#             else:
#                 if usr_rating < 0 or usr_rating > 5:
#                     print("Error: Rating out of bounds. Please rate the melody from 0-5")
#                 else:
#                     break

#     return usr_rating,

# #melody = Melody()
# #ret_tup = evaluate_music(melody)
# #print(ret_tup)
# import mido
# from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo, second2tick, tempo2bpm
# from representation import Measure, Note, MIDI_TO_NOTE, MEASURES_P_MELODY, BEATS_P_MEASURE

# outport = mido.open_output(None)
# melody = Melody()
# #play(melody)
# #print(melody)
# original_str = str(melody)
# melody_to_midi(melody, 'program_melody2.mid', 100)
# mid_file = MidiFile('/Users/dannynoe/Documents/URI/CSC 499/Project/Code/midi_out/program_melody2.mid')


# tempo = 0
# key_signature = ""
# for message in mid_file.play(True):
#     print(message)
#     if message.is_meta:
#         print("meta")
#         if message.type == 'key_signature':
#             key_signature = message.key
#         elif message.type == 'set_tempo':
#             tempo = message.tempo
#     else:
#         break
#         #outport.send(message)


# # Convert MIDI time to micro-seconds 60000 / (BPM * PPQ) PPQ = ticks_per_beat

# print(mid_file.length)
# print(mid_file.ticks_per_beat)
# ticks_per_beat = mid_file.ticks_per_beat
# tempo = int(tempo2bpm(tempo) + 0.5)
# print(tempo)
# seconds_per_tick =  (60000 / (tempo * ticks_per_beat)) / 1000000
# print(seconds_per_tick)
# note_list = []
# rest = False
# sum_beats = 0.0
# for message in mid_file:
#     print(message)
#     if message.is_meta:
#         print("meta")
#         pass
#     else:
#         print("Note")
#         if message.time != 0:
#             if rest:
#                 pass
#                 n_p = "Rest"
#                 rest = False
#             else:
#                 n_p = message.note
#             vel = message.velocity
#             time = message.time
#             ticks = time / seconds_per_tick
#             beats = ticks / ticks_per_beat
#             beats = beats / 1000
#             beats = round(beats, 2)
#             sum_beats += beats
#             note_list.append(Note(n_p, beats, vel))
#         elif message.type == 'note_off':
#             rest = True
#         else:
#             pass

# read_str = ""        
# for note in note_list:
#     read_str += str(note) + '\n'
#     print(note)

# print("Original melody")
# print(original_str)
# print("Read string")
# print(read_str)

# print(sum_beats)

# measure_list = []
# melody_list = []
# sum_beats = 0.0
# for note in note_list:
#     # if sum_beats < BEATS_P_MEASURE:
#     #     sum_beats += note.beats
#     #     measure_list.append(note)
#     # else:
#     #     melody_list.append(Measure(measure_list))
#     #     sum_beats = 0.0
#     #     measure_list = []
#     sum_beats += note.beats
#     measure_list.append(note)
#     if sum_beats == BEATS_P_MEASURE:
#         melody_list.append(Measure(measure_list))
#         sum_beats = 0.0
#         measure_list = []

#     print(note)

# print("Playing original:")
# play(melody)

# melody_read_from_mid = Melody(melody_list)
# print("Play read from file:")
# play(melody_read_from_mid)


# filename = ""
# if filename:
#     print("True")
# else:
#     print("Filename is none")

# print("Done.")