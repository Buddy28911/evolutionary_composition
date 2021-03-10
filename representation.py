# Representation.py
# By Danny Noe

import random
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo

BEATS_P_MEASURE = 4.0
MEASURES_P_MELODY = 2
KEY = "C"
TEMPO = 120 # BPM
NOTE_RANGE = ["C4", "C4#", "D4", "D4#", "E4", "F4", "F4#", "G4", "G4#", "A4", "A4#", "B4", "C5", 
            "C5#", "D5", "D5#", "E5", "F5", "F5#", "G5", "G5#", "A5", "A5#", "B5", 'C6', "Rest"]

NOTE_TO_MIDI = {'C4': 60, 'C4#': 61, 'D4': 62, 'D4#': 63, 'E4': 64, 'F4': 65, 'F4#': 66, 'G4': 67, 
                'G4#': 68, 'A4': 69, 'A4#': 70, 'B4': 71, 'C5': 72, 'C5#': 73, 'D5': 74, 'D5#': 75, 
                'E5': 76, 'F5': 77, 'F5#': 78, 'G5': 79, 'G5#': 80, 'A5': 81, 'A5#': 82, 'B5': 83, 
                'C6': 84, 'Rest': 128}

MIDI_TO_NOTE = {60: 'C4', 61: 'C4#', 62: 'D4', 63: 'D4#', 64: 'E4', 65: 'F4', 66: 'F4#', 67: 'G4', 
                68: 'G4#', 69: 'A4', 70: 'A4#', 71: 'B4', 72: 'C5', 73: 'C5#', 74: 'D5', 75: 'D5#', 
                76: 'E5', 77: 'F5', 78: 'F5#', 79: 'G5', 80: 'G5#', 81: 'A5', 82: 'A5#', 83: 'B5', 
                84: 'C6', 128: 'Rest'}

BEAT_VALUES = [2.0, 1.0, 0.5, 0.25] # Note: Whole notes have been removed for now

class Note:
    """
    The Note class represents a western music note. It has two attributes.
    A note_pitch which is a string representing the pitch of the note
    A beats float representing the length of the note. Currently supports: whole, half, quarter, eighth and sixteenth notes
    """
    def __init__(self, note_pitch: int = None, beats: float = None):
        """
        Initializes a Note class member. Can be initialized with specific values or have
        its attributes randomly assigned upon initialization.
        """

        if note_pitch is None:
            note_str = random.choice(NOTE_RANGE)
            note_pitch = NOTE_TO_MIDI[note_str] # Assign note a value if none is given
        elif note_pitch not in NOTE_RANGE:
            raise Exception("Error: %s Out of note range and not a rest", note_pitch)
            # Ensures a given pitch is in the define range

        if beats is None:
            beats = random.choice(BEAT_VALUES)    # Assign the note a length if non is given
        elif beats not in BEAT_VALUES:
            raise Exception("Error: %f Invalid number of beats", beats)
            # Ensures a given beat is within range

        self.note_pitch = note_pitch
        self.beats = beats
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
        return "Pitch: " + MIDI_TO_NOTE[self.note_pitch] + "| Beats: " + str(self.beats)

class Measure:
    """
    The Measure class represents a measure in musical notation. The measure class
    has on attribute. The member measure_list is a list of Note classes in the measure.
    The measure class ensures the length of all notes in the measures = BEATS_P_MEASURE
    """
    def __init__(self):
        """
        Measures class objects are initialized by randomly generating notes until the measure_list
        has reached a length of BEATS_P_MEASURE
        """
        self.measure_list = []
        total_beats = 0.0
        while total_beats != BEATS_P_MEASURE:
            current_beat = random.choice(BEAT_VALUES)
            while total_beats + current_beat > BEATS_P_MEASURE:
                current_beat = random.choice(BEAT_VALUES)
            new_note = Note(beats=current_beat)
            self.measure_list.append(new_note)
            total_beats += current_beat
        return
        
    def __str__(self):
        """
        To string method for Measure class. For debugging.
        """
        to_str = "Notes in Measure:\n"
        for m_note in self.measure_list:
            to_str += str(m_note) + "\n"
        return to_str

class Melody:
    """
    The Melody class represents a musical melody. Melodies contain a list of measures.
    The number of measures in a melody are defined by MEASURES_P_MELODY.
    The Melody class's only attribute is the melody_list list of measures.
    """
    def __init__(self, melody_list = None):
        """
        Initalizes a Melody object with MEASURES_P_MELODY amount of measures
        """
        if melody_list is None:
            self.melody_list = []
            for i in range(MEASURES_P_MELODY):
                #print(i)
                new_measure = Measure()
                self.melody_list.append(new_measure)
            return
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
        return Melody(melody_list=self.melody_list)

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
            
def melody_to_midi(melody: Melody, filename: str, tempo: int):
    mid = MidiFile(type=0)
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(MetaMessage('key_signature', key=KEY))
    tempo = bpm2tempo(tempo)
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
    ticks_per_beat = mid.ticks_per_beat
    
    for measure in melody.melody_list:
        for note in measure.measure_list:
            beat_val = note.beats * ticks_per_beat
            beat_val = int(beat_val)
            if note.note_pitch == 128:
                # Rest
                track.append(Message('note_off', note=60, velocity=127, time=0))
                track.append(Message('note_off', note=60, velocity=127, time=beat_val))

            else:
                # Note on
                track.append(Message('note_on', note=note.note_pitch, velocity=64, time=0))
                track.append(Message('note_off', note=note.note_pitch, velocity=127, time=beat_val))

    mid.save(filename)
    return

def play(melody: Melody, outport = None):
    
    mid = MidiFile(type=0)
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(MetaMessage('key_signature', key=KEY))
    tempo = bpm2tempo(TEMPO)
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
    ticks_per_beat = mid.ticks_per_beat
    
    for measure in melody.melody_list:
        for note in measure.measure_list:
            beat_val = note.beats * ticks_per_beat
            beat_val = int(beat_val)
            if note.note_pitch == 128:
                # Rest
                track.append(Message('note_off', note=60, velocity=127, time=0))
                track.append(Message('note_off', note=60, velocity=127, time=beat_val))

            else:
                # Note on
                track.append(Message('note_on', note=note.note_pitch, velocity=64, time=0))
                track.append(Message('note_off', note=note.note_pitch, velocity=127, time=beat_val))
    
    outport = mido.open_output(outport)
    for message in mid.play():
        outport.send(message)
    return

# melody = Melody()
# play(melody)

# outport = mido.open_output(None)
# melody = Melody()
# print(melody)
# melody_to_midi(melody, './Project/Code/new_mid.mid', 164)
# for message in MidiFile('./Project/Code/new_mid.mid').play():
#     print(message)
#     outport.send(message)
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