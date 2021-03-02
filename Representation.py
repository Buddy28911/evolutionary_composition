import random

BEATS_P_MEASURE = 4.0
MEASURES_P_MELODY = 2
KEY = "C"
NOTE_RANGE = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5", "C6", "Rest"]
            # Treble Clef range
BEAT_VALUES = [4.0, 2.0, 1.0, 0.5, 0.25]

class Note:
    """
    The Note class represents a western music note. It has two attributes.
    A note_pitch which is a string representing the pitch of the note
    A beats float representing the length of the note. Currently supports: whole, half, quarter, eighth and sixteenth notes
    """
    def __init__(self, note_pitch: str = None, beats: float = None):
        """
        Initializes a Note class member. Can be initialized with specific values or have
        its attributes randomly assigned upon initialization.
        """

        if note_pitch is None:
            note_pitch = random.choice(NOTE_RANGE) # Assign note a value if none is given
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

    def get_pitch(self):
        """
        Returns the notes pitch value as a str
        """
        return self.note_pitch

    def get_beats(self):
        """
        Returns the note's length in beats as a float
        """
        return self.beats

    def __str__(self):
        """
        To string method for printing notes. For debugging
        """
        return "Pitch: " + self.note_pitch + "| Beats: " + str(self.beats)

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
    def __init__(self):
        """
        Initalizes a Melody object with MEASURES_P_MELODY amount of measures
        """
        self.melody_list = []
        for i in range(MEASURES_P_MELODY):
            print(i)
            new_measure = Measure()
            self.melody_list.append(new_measure)
        return

    def __str__(self):
        """
        To string method for melody class. Returns a string representation of a melody. For debugging
        """
        to_str = "Melody:\n"
        for msr in self.melody_list:
            to_str += str(msr)
        return to_str
            

test_note_1 = Note("C4", 1.0)
print(test_note_1)
test_note_2 = Note("Rest", 2.0)
print(test_note_2)
rand_note = Note()
print(rand_note)
print(rand_note.note_pitch)

FirstM = Measure()
print("Notes in list:")
for m_note in FirstM.measure_list:
    print(m_note)

print(FirstM)

mel1 = Melody()
print(mel1)