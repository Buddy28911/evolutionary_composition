# Representation.py
# By Danny Noe

import random
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo, tempo2bpm
from music_data import *

class representation:
    """
    Container class, only one instance is created for the program. Used to store config information
    """
    
    def __init__(self, key_signature: str, tempo: int, back_track: bool, arp_or_scale: bool, outport: str):
        self.key_signature = key_signature
        self.tempo = tempo
        self.back_track = back_track
        self.arp_or_scale = arp_or_scale
        self.outport = outport
        return
         
    def melody_to_midi(self, melody, filename: str, play: bool):
        mid = MidiFile(type=1)
        track = MidiTrack(name="Lead")
        mid.tracks.append(track)
        track.append(MetaMessage('key_signature', key=self.key_signature))
        tempo = bpm2tempo(self.tempo)
        track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
        ticks_per_beat = mid.ticks_per_beat
        
        for measure in melody.melody_list:
            for note in measure.measure_list:
                beat_val = note.beats * ticks_per_beat
                beat_val = int(beat_val)
                if note.note_pitch == 128:
                    # Rest
                    track.append(Message('note_off', note=60, velocity=note.velocity, time=0))
                    track.append(Message('note_off', note=60, velocity=note.velocity, time=beat_val))

                else:
                    # Note on
                    track.append(Message('note_on', note=note.note_pitch, velocity=note.velocity, time=0))
                    track.append(Message('note_off', note=note.note_pitch, velocity=0, time=beat_val))
        
        # Backing Track
        if self.back_track:
            self.add_backing_track(mid)
        
        if play:
            outport = mido.open_output(self.outport)
            for message in mid.play():
                outport.send(message)
        
        if filename:
            filename = "./midi_out/" + filename
            mid.save(filename)

        return

    def add_backing_track(self, mid: MidiFile):
        """
        Input: A multitrack MidiFile object
        Output: Adds a backing track to the midifile. Adds either a scale or arpeggio
        """
        ticks_per_beat = mid.ticks_per_beat
        backing_track = MidiTrack(name="Backing")
        mid.tracks.append(backing_track)
        length_of_background = (int(BEATS_P_MEASURE) * MEASURES_P_MELODY * 2)
        #print(length_of_background)
        
        scale = SCALES[self.key_signature]
        if self.arp_or_scale:
            for beat in range(length_of_background):
                ar_pitch = NOTE_TO_MIDI[scale[0]]
                if (beat % 4) == 1:
                    ar_pitch = NOTE_TO_MIDI[scale[2]]
                elif (beat % 4) == 2:
                    ar_pitch = NOTE_TO_MIDI[scale[4]]
                elif (beat % 4) == 3:
                    ar_pitch = NOTE_TO_MIDI[scale[7]]
                backing_track.append(Message('note_on', note=ar_pitch, velocity=42, time=0))
                ar_beat = 0.5 * ticks_per_beat
                ar_beat = int(ar_beat)
                backing_track.append(Message('note_off', note=ar_pitch, velocity=0, time=ar_beat))
        else:
            step = 0
            for beat in range(length_of_background):
                ar_pitch = NOTE_TO_MIDI[scale[step]]
                backing_track.append(Message('note_on', note=ar_pitch, velocity=42, time=0))
                ar_beat = 0.5 * ticks_per_beat
                ar_beat = int(ar_beat)
                backing_track.append(Message('note_off', note=ar_pitch, velocity=0, time=ar_beat))
                step += 1
                if step >= 8:
                    step = 0

        return

    def evaluate_music(self, input_mel):
        """
        Evaluation function for music that evaluates a given melody
        """
        print("Playing Melody ...")
        self.melody_to_midi(input_mel, None, True)

        evaluating = True
        while evaluating:
            # Handle the user's input
            usr_string = input("Did you enjoy that little diddy? Please rate from 0-5 (ints only). To hear it again type replay: ")
            if usr_string.lower() == "replay":
                print("Playing Melody ...")
                self.melody_to_midi(input_mel, None, True)
            else:
                try:
                    usr_rating = int(usr_string)
                except ValueError:
                    print("Error: Invalid input. Please rate the melody from 0-5 or enter replay to hear it again: ")
                else:
                    if usr_rating < 0 or usr_rating > 5:
                        print("Error: Rating out of bounds. Please rate the melody from 0-5")
                    else:
                        evaluating = False
                        break

        return usr_rating,


# Note Class
class Note:
    """
    The Note class represents a western music note. It has two attributes.
    A note_pitch which is a string representing the pitch of the note
    A beats float representing the length of the note. Currently supports: whole, half, quarter, eighth and sixteenth notes
    """
    def __init__(self, note_pitch = None, beats: float = None, velocity: int = None):
        """
        Initializes a Note class member. Can be initialized with specific values or have
        its attributes randomly assigned upon initialization.
        """

        if note_pitch is None:
            note_str = random.choice(NOTE_RANGE)
            note_pitch = NOTE_TO_MIDI[note_str] # Assign note a value if none is given
        else:
            if type(note_pitch) is str:
                if note_pitch not in NOTE_RANGE:
                    raise Exception("Error:", note_pitch, " out of note range and not a rest")
                    # Ensures a given pitch is in the define range
                else:
                    note_pitch = NOTE_TO_MIDI[note_pitch]
            elif type(note_pitch) is int:
                if MIDI_TO_NOTE[note_pitch]  not in NOTE_RANGE:
                    raise Exception("Error:", note_pitch, " out of note range and not a rest")
            else:
                raise Exception("Error:", note_pitch, " must be a string or int")

        if beats is None:
            beats = random.choice(BEAT_VALUES)    # Assign the note a length if none is given
        elif beats not in BEAT_VALUES:
            raise Exception("Error: %f Invalid number of beats", beats)
            # Ensures a given beat is within range

        if velocity is None:
            velocity = random.choice(VELOCITY_RANGE)
        elif velocity < 0 or velocity > 127:
            raise Exception("Error: Velocity out of bounds. Range 0-127")

        self.note_pitch = note_pitch
        self.beats = beats
        self.velocity = velocity
        return

    def pitch_shift(self, increment = 1,  up = True):
        if up:
            # Shift pitch up # increment semitones
            self.note_pitch += increment
        else:
            # Shifts pitch down # increment semitones
            self.note_pitch -= increment
            pass
        return

    def __str__(self):
        """
        To string method for printing notes. For debugging
        """
        return "Pitch: " + MIDI_TO_NOTE[self.note_pitch] + " | Beats: " + str(self.beats) + " | Velocity: " + str(self.velocity)

# Measure Class
class Measure:
    """
    The Measure class represents a measure in musical notation. The measure class
    has on attribute. The member measure_list is a list of Note classes in the measure.
    The measure class ensures the length of all notes in the measures = BEATS_P_MEASURE
    """
    def __init__(self, measure_list: list = None):
        """
        Measures class objects are initialized by randomly generating notes until the measure_list
        has reached a length of BEATS_P_MEASURE
        """
        
        self.measure_list = []
        if measure_list is None:
            total_beats = 0.0
            while total_beats != BEATS_P_MEASURE:
                current_beat = random.choice(BEAT_VALUES)
                while total_beats + current_beat > BEATS_P_MEASURE:
                    current_beat = random.choice(BEAT_VALUES)
                new_note = Note(beats=current_beat)
                self.measure_list.append(new_note)
                total_beats += current_beat
            return
        else:
            total_beats = 0.0
            for note in measure_list:
                total_beats += note.beats
                if total_beats > BEATS_P_MEASURE:
                    raise Exception("Error: Number of beats in given list greater than ", BEATS_P_MEASURE, " ", total_beats)
                else:
                    self.measure_list.append(note)
            return
        
    def __str__(self):
        """
        To string method for Measure class. For debugging.
        """
        to_str = "Notes in Measure:\n"
        for m_note in self.measure_list:
            to_str += str(m_note) + "\n"
        return to_str

# Melody Class
class Melody:
    """
    The Melody class represents a musical melody. Melodies contain a list of measures.
    The number of measures in a melody are defined by MEASURES_P_MELODY.
    The Melody class's only attribute is the melody_list list of measures.
    """
    def __init__(self, key: str, melody_list = None, filename = None):
        """
        Initalizes a Melody object with MEASURES_P_MELODY amount of measures
        """
        self.key = key
        if filename is not None and melody_list is not None:
            raise Exception("Error: Only a melody_list or filename can be given")

        if filename:
            filename = "./midi_out/" + filename
            mid_file = MidiFile(filename)
            self.melody_list = midi_to_melody(mid_file)
            return

        elif melody_list is None:
            self.melody_list = new_melody(self.key)
            # for i in range(MEASURES_P_MELODY):
            #     #print(i)
            #     new_measure = Measure()
            #     self.melody_list.append(new_measure)

        else:
            if len(melody_list) > MEASURES_P_MELODY:
                raise Exception("Error: Melody longer than ", MEASURES_P_MELODY)
            else:
                self.melody_list = melody_list

        return

    def len(self):
        """
        Returns the number of measures in the melody as an int
        """
        return len(self.melody_list)

    def copy(self):
        """
        Returns a new melody object that is a copy the current melody object
        """
        return Melody(self.key, melody_list=self.melody_list)

    def cross_mel(self, mel2, change_first_half):
        """
        
        """
        if change_first_half:
            # Swap first half of melody for mel2's first half
            end = MEASURES_P_MELODY // 2
            i = 0
            while i < end:
                self.melody_list[i] = mel2.melody_list[i]
                i += 1
            pass
        else:
            # Swap second half of melody for mel2's second half
            i = MEASURES_P_MELODY // 2
            while i < MEASURES_P_MELODY:
                self.melody_list[i] = mel2.melody_list[i]
                i += 1
            pass
        return

    def __str__(self):
        """
        To string method for melody class. Returns a string representation of a melody. For debugging
        """
        to_str = "Melody:\n"
        for msr in self.melody_list:
            to_str += str(msr)
        return to_str


def shift_scale(key: str) -> list:
    """
    Returns list of notes in a scale shifted up two octaves
    Input: key: str, the key used to get the scale from the SCALES dict
    Output: shifted_scale: list, list of 8 notes shifted up two octaves
    """
    scale = SCALES[key]
    shifted_scale = []

    for ori_note in scale:
        num = int(ori_note[1]) + 2
        shifted_note = ori_note[0] + str(num)
        if len(ori_note) == 3:
            shifted_note += ori_note[2]
        shifted_scale.append(shifted_note)

    return shifted_scale

def get_new_pitch(prev_pitch: int, interval: int, ascend_or_descend: int) -> int:
    """
    Returns a new_pitch based off the prev_pitch
    Input: prev_pitch: int, the previous pitch | interval: int, the interval to shift the new_pitch | ascend_or_descend: int, dictates if the pitch is shifted up or down
    Output: new_pitch: int, shifted pitch
    """
    upper_bound = 84 - interval
    lower_bound = 60 + interval
    new_pitch = 0

    if prev_pitch > upper_bound:
        # Override the ascend_or_descend val if we are at the bound
        new_pitch = prev_pitch - interval
    elif prev_pitch < lower_bound:
        # Override the ascend_or_descend val if we are at the bound
        new_pitch = prev_pitch + interval
    elif ascend_or_descend == 0:
        new_pitch = prev_pitch - interval
    else:
        new_pitch = prev_pitch - interval

    return new_pitch


def get_new_note_pitch(prev_pitch: int):

    # Will be called from next_note
    new_pitch = 0
    if prev_pitch == 128:
        # If the previous 2 notes are rests, random new note
        option = 6
    else:
        # Else the previous pitch could impact new pitch
        option = random.randint(0, 7)

    ascend_or_descend = random.randint(0, 1) # Ascend = 1, Descend = 1

    if option == 0:
        # repeat
        new_pitch = prev_pitch
    elif option == 1:
        # step
        new_pitch = get_new_pitch(prev_pitch, 2, ascend_or_descend)

    elif option == 2:
        # third
        new_pitch = get_new_pitch(prev_pitch, 3, ascend_or_descend)

    elif option == 3:
        # skip
        skip = random.randint(1, 4)
        new_pitch = get_new_pitch(prev_pitch, skip, ascend_or_descend)

    elif option == 4:
        # Octave
        new_pitch = get_new_pitch(prev_pitch, 12, ascend_or_descend)

    elif option == 5:
        # jump
        jump = random.randint(4, 14)
        new_pitch = get_new_pitch(prev_pitch, jump, ascend_or_descend)

    elif option == 6:
        # random
        new_pitch = random.choice(NOTE_RANGE)

    elif option == 7:
        # rest
        new_pitch = 128

    return

def get_new_note_beat(measure_beats: float):

    # Will be called from next_note
    current_beat = random.choice(BEAT_VALUES)
    while measure_beats + current_beat > BEATS_P_MEASURE:
            current_beat = random.choice(BEAT_VALUES)
    return current_beat

def get_new_note_velocity():
    # Will be called from next_note
    return random.choice(VELOCITY_RANGE)

def next_note(prev: Note, measure_beats: int):
    # Will be called from new_melody
    new_note_list = [0, 0.0, 0] # Note, Beats, Velocity

    new_note_list[0] = get_new_note_pitch(prev.note_pitch)
    
    new_note_list[1] = get_new_note_beat(measure_beats)

    new_note_list[2] = get_new_note_velocity()
    return new_note_list

def new_melody(key):
    note_list = []
    sum_beats = 0.0
    max_beats = BEATS_P_MEASURE * MEASURES_P_MELODY * 1.0
    scale = shift_scale(key) # Shift the scale to the treble clef range
    note_index = 0
    new_note_list = [0, 0.0, 0] # Note, Beats, Velocity
    new_measure = True
    measure_beats = 0.0
    while sum_beats < max_beats:
            
        if note_index == 0:
            # Initial case
            new_note_list[0] = scale[random.randint(2, 7)] # Set the starting pitch within the scale
            new_note_list[1] = random.choice([2.0, 1.0]) # Start melody on longer notes
            new_note_list[2] = random.choice(VELOCITY_RANGE) #Allow any velocity
        else:
            # Normal case
            prev = note_list[note_index-1]
            if prev.note_pitch == 128 and len(note_list) > 2:
                # If the previous pitch was a rest, refer to the pitch at note_index-2
                prev = note_list[note_index-2]
                
            # Where new_note returns
            new_note_list = next_note(prev, measure_beats)
        
        note_list.append(Note(new_note_list[0], new_note_list[1], new_note_list[2]))
        sum_beats += new_note_list[1]
        measure_beats += new_note_list[1]
        if measure_beats == BEATS_P_MEASURE:
            measure_beats = 0.0
        note_index += 1
        new_note_list = [0, 0.0, 0] # Note, Beats, Velocity
        
    return build_melody(note_list)

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
            
def save_list_of_melodies(rep_obj, the_mel_list, group_name, mel_num):
    for melody in the_mel_list:
        filename = group_name + str(mel_num) + ".mid"
        rep_obj.melody_to_midi(melody, filename, False)
        mel_num += 1
    return mel_num

def save_best_melodies(rep_obj, population, hall_of_fame):
    mel_num = 0
    mel_num = save_list_of_melodies(rep_obj, population, "population", mel_num)
    mel_num = save_list_of_melodies(rep_obj, hall_of_fame, "hall_of_fame", mel_num)
    return

# melody = Melody()
# #play(melody)
# melody_to_midi(melody, None, TEMPO, True)
# melody_to_midi(melody, 'arp_test2.mid', TEMPO, False)
# mid_to_mel = Melody(filename='program_mid3.mid')
# melody_to_midi(mid_to_mel, 'program_mid4.mid', 90)
#play(mid_to_mel)


# outport = mido.open_output(None)
# melody = Melody()
# print(melody)
# melody_to_midi(melody, './Project/Code/new_mid.mid', 164)
# for message in MidiFile('./Project/Code/new_mid.mid').play():
#     print(message)
#     outport.send(message)

# def play(melody: Melody, outport = None):
    
#     mid = MidiFile(type=1)
#     track = MidiTrack()
#     mid.tracks.append(track)
#     track.append(MetaMessage('key_signature', key=KEY))
#     tempo = bpm2tempo(TEMPO)
#     track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
#     ticks_per_beat = mid.ticks_per_beat
    
#     for measure in melody.melody_list:
#         for note in measure.measure_list:
#             beat_val = note.beats * ticks_per_beat
#             beat_val = int(beat_val)
            
#             if note.note_pitch == 128:
#                 # Rest
#                 track.append(Message('note_off', note=60, velocity=note.velocity, time=0))
#                 track.append(Message('note_off', note=60, velocity=note.velocity, time=beat_val))

#             else:
#                 # Note on
#                 track.append(Message('note_on', note=note.note_pitch, velocity=note.velocity, time=0))
#                 track.append(Message('note_off', note=note.note_pitch, velocity=0, time=beat_val))
    
#     # Backing Track
#     backing_track = MidiTrack()
#     mid.tracks.append(backing_track)
#     length_of_background = (int(BEATS_P_MEASURE) * MEASURES_P_MELODY * 2)
#     #print(length_of_background)
#     #C3 48, E3 52, G3 55, C4 60
#     for beat in range(length_of_background *2):
#         ar_pitch = 48
#         if (beat % 4) == 1:
#             ar_pitch = 52
#         elif (beat % 4) == 2:
#             ar_pitch = 55
#         elif (beat % 4) == 3:
#             ar_pitch = 60
#         backing_track.append(Message('note_on', note=ar_pitch, velocity=42, time=0))
#         ar_beat = 0.25 * ticks_per_beat
#         backing_track.append(Message('note_off', note=ar_pitch, velocity=0, time=ar_beat))

#     outport = mido.open_output(outport)
#     for message in mid.play():
#         outport.send(message)
#     return
"""
# test_note_1 = Note("C4", 1.0)
# print(test_note_1)
# test_note_2 = Note("Rest", 2.0)
# print(test_note_2)
# rand_note = Note()
# print(rand_note)
# print(rand_note.note_pitch)

# FirstM = Measure()
# print("Notes in list:")
# for m_note in FirstM.measure_list:
#     print(m_note)

# print(FirstM)

# mel1 = Melody()
# print(mel1)
#print(mido.get_output_names())
#outport = mido.open_output('IAC Driver Bus 1')
# note = Note(note_pitch="C5", beats=1.0)
# print(note)
# val = NOTE_TO_MIDI[note.get_pitch()]
# msg = mido.Message('note_on', velocity=127, note=val, time=0)
# print(msg)
# outport.send(msg)
# msg2 = mido.Message('note_off', velocity=127, note=val, time=0)
# print(msg2)
# outport.send(msg2)
# msg3 = mido.Message('note_on', velocity=127, note=65, time=1)
# outport.send(msg3)


### MIDI File testing
# mid = MidiFile(type=0)
# track = MidiTrack()
# mid.tracks.append(track)
# track.append(MetaMessage('key_signature', key='C'))
# tempo = bpm2tempo(100)
# track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
# ticks_per_beat = mid.ticks_per_beat
# mellody1 = Melody()
# for measure in mellody1.melody_list:
#     for note in measure.measure_list:
#         if note.note_pitch != 'Rest':
#             midi_val = NOTE_TO_MIDI[note.note_pitch]
#         else:
#             midi_val = 72
#         beat_val = note.beats * ticks_per_beat
#         beat_val = int(beat_val)
#         print(beat_val)
#         track.append(Message('note_on', note=midi_val, velocity=64, time=0))
#         track.append(Message('note_off', note=midi_val, velocity=127, time=beat_val))

# mid.save('./Project/Code/new_mid.mid')

# melody = Melody()
# melody_to_midi(melody, './Project/Code/new_mid.mid', 164)
# for message in MidiFile('./Project/Code/new_mid.mid').play():
#     print(message)
#     outport.send(message)



### MIDI File testing
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo
mid = MidiFile(type=0)
track = MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('key_signature', key='C'))
tempo = bpm2tempo(200)
track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
mid.ticks_per_beat = 240
tim = 240
for i in range(26):
    track.append(Message('note_on', note=60+i, velocity=64, time=0))
    #tim += 64
    track.append(Message('note_off', note=60+i, velocity=127, time=240))
    track.append(Message('note_off', note=60+i, velocity=127, time=0))
    track.append(Message('note_off', note=60+i, velocity=127, time=240))

    #tim += 64

mid.save('./Project/Code/new_mid.mid')

for message in MidiFile('./Project/Code/new_mid.mid').play():
    print(message)
    outport.send(message)
"""