# music_date.py
# Danny Noe
# Evolutionary Composition
# music_data.py houses constant data used by representation.py. This file has no executable code

##############################
# Representation specific data
##############################
BEATS_P_MEASURE = 4.0
MEASURES_P_MELODY = 4
#KEY = "Bb"
#TEMPO = 90 # BPM
BEAT_VALUES = [2.0, 1.0, 0.5, 0.25] # Note: Whole and 32nd notes could be supported, but are not due to the melodies being short
VELOCITY_RANGE = [53, 64, 80, 96] # MP, MF, F, FF
#ARP_OR_SCA = False # True = Arp, False = Scale

NOTE_RANGE = ["C4", "C4#", "D4", "D4#", "E4", "F4", "F4#", "G4", "G4#", "A4", "A4#", "B4", "C5", 
            "C5#", "D5", "D5#", "E5", "F5", "F5#", "G5", "G5#", "A5", "A5#", "B5", 'C6',
            "Rest", "Rest", "Rest", "Rest"] # Treble clef range

##############################
# MIDI specific data
##############################
MIDI_RANGE = ["C0", "C0#", "D0", "D0#", "E0", "F0", "F0#", "G0", "G0#", "A0", "A0#", "B0",
            "C1", "C1#", "D1", "D1#", "E1", "F1", "F1#", "G1", "G1#", "A1", "A1#", "B1",
            "C2", "C2#", "D2", "D2#", "E2", "F2", "F2#", "G2", "G2#", "A2", "A2#", "B2",
            "C3", "C3#", "D3", "D3#", "E3", "F3", "F3#", "G3", "G3#", "A3", "A3#", "B3",
            "C4", "C4#", "D4", "D4#", "E4", "F4", "F4#", "G4", "G4#", "A4", "A4#", "B4", 
            "C5", "C5#", "D5", "D5#", "E5", "F5", "F5#", "G5", "G5#", "A5", "A5#", "B5", 
            "C6", "C6#", "D6", "D6#", "E6", "F6", "F6#", "G6", "G6#", "A6", "A6#", "B6",
            "C7", "C7#", "D7", "D7#", "E7", "F7", "F7#", "G7", "G7#", "A7", "A7#", "B7",
            "C8", "C8#", "D8", "D8#", "E8", "F8", "F8#", "G8", "G8#", "A8", "A8#", "B8",
            "C9", "C9#", "D9", "D9#", "E9", "F9", "F9#", "G9"]

NOTE_TO_MIDI = {'C0': 12, 'C0#': 13, 'D0': 14, 'D0#': 15, 'E0': 16, 'F0': 17, 'F0#': 18, 'G0': 19, 'G0#': 20, 'A0': 21, 'A0#': 22, 'B0': 23, 
                'C1': 24, 'C1#': 25, 'D1': 26, 'D1#': 27, 'E1': 28, 'F1': 29, 'F1#': 30, 'G1': 31, 'G1#': 32, 'A1': 33, 'A1#': 34, 'B1': 35, 
                'C2': 36, 'C2#': 37, 'D2': 38, 'D2#': 39, 'E2': 40, 'F2': 41, 'F2#': 42, 'G2': 43, 'G2#': 44, 'A2': 45, 'A2#': 46, 'B2': 47, 
                'C3': 48, 'C3#': 49, 'D3': 50, 'D3#': 51, 'E3': 52, 'F3': 53, 'F3#': 54, 'G3': 55, 'G3#': 56, 'A3': 57, 'A3#': 58, 'B3': 59, 
                'C4': 60, 'C4#': 61, 'D4': 62, 'D4#': 63, 'E4': 64, 'F4': 65, 'F4#': 66, 'G4': 67, 'G4#': 68, 'A4': 69, 'A4#': 70, 'B4': 71, 
                'C5': 72, 'C5#': 73, 'D5': 74, 'D5#': 75, 'E5': 76, 'F5': 77, 'F5#': 78, 'G5': 79, 'G5#': 80, 'A5': 81, 'A5#': 82, 'B5': 83, 
                'C6': 84, 'C6#': 85, 'D6': 86, 'D6#': 87, 'E6': 88, 'F6': 89, 'F6#': 90, 'G6': 91, 'G6#': 92, 'A6': 93, 'A6#': 94, 'B6': 95, 
                'C7': 96, 'C7#': 97, 'D7': 98, 'D7#': 99, 'E7': 100, 'F7': 101, 'F7#': 102, 'G7': 103, 'G7#': 104, 'A7': 105, 'A7#': 106, 'B7': 107, 
                'C8': 108, 'C8#': 109, 'D8': 110, 'D8#': 111, 'E8': 112, 'F8': 113, 'F8#': 114, 'G8': 115, 'G8#': 116, 'A8': 117, 'A8#': 118, 'B8': 119, 
                'C9': 120, 'C9#': 121, 'D9': 122, 'D9#': 123, 'E9': 124, 'F9': 125, 'F9#': 126, 'G9': 127, 'Rest': 128}

MIDI_TO_NOTE = {12: 'C0', 13: 'C0#', 14: 'D0', 15: 'D0#', 16: 'E0', 17: 'F0', 18: 'F0#', 19: 'G0', 20: 'G0#', 21: 'A0', 22: 'A0#', 23: 'B0', 
                24: 'C1', 25: 'C1#', 26: 'D1', 27: 'D1#', 28: 'E1', 29: 'F1', 30: 'F1#', 31: 'G1', 32: 'G1#', 33: 'A1', 34: 'A1#', 35: 'B1', 
                36: 'C2', 37: 'C2#', 38: 'D2', 39: 'D2#', 40: 'E2', 41: 'F2', 42: 'F2#', 43: 'G2', 44: 'G2#', 45: 'A2', 46: 'A2#', 47: 'B2', 
                48: 'C3', 49: 'C3#', 50: 'D3', 51: 'D3#', 52: 'E3', 53: 'F3', 54: 'F3#', 55: 'G3', 56: 'G3#', 57: 'A3', 58: 'A3#', 59: 'B3', 
                60: 'C4', 61: 'C4#', 62: 'D4', 63: 'D4#', 64: 'E4', 65: 'F4', 66: 'F4#', 67: 'G4', 68: 'G4#', 69: 'A4', 70: 'A4#', 71: 'B4', 
                72: 'C5', 73: 'C5#', 74: 'D5', 75: 'D5#', 76: 'E5', 77: 'F5', 78: 'F5#', 79: 'G5', 80: 'G5#', 81: 'A5', 82: 'A5#', 83: 'B5', 
                84: 'C6', 85: 'C6#', 86: 'D6', 87: 'D6#', 88: 'E6', 89: 'F6', 90: 'F6#', 91: 'G6', 92: 'G6#', 93: 'A6', 94: 'A6#', 95: 'B6', 
                96: 'C7', 97: 'C7#', 98: 'D7', 99: 'D7#', 100: 'E7', 101: 'F7', 102: 'F7#', 103: 'G7', 104: 'G7#', 105: 'A7', 106: 'A7#', 107: 'B7', 
                108: 'C8', 109: 'C8#', 110: 'D8', 111: 'D8#', 112: 'E8', 113: 'F8', 114: 'F8#', 115: 'G8', 116: 'G8#', 117: 'A8', 118: 'A8#', 119: 'B8', 
                120: 'C9', 121: 'C9#', 122: 'D9', 123: 'D9#', 124: 'E9', 125: 'F9', 126: 'F9#', 127: 'G9', 128: 'Rest'}

##############################
# Scales
##############################
# Currently all major scales supported by MIDI are implemented. Minor scales are not currently implemented
SCALES = {"Cb": ["B2", "C3#", "D3#", "E3", "F3#", "G3#", "A3#", "B3"],
        "Gb": ["F2#", "G2#", "A2#", "B2", "C3#", "D3#", "F3", "F3#"],
        "Db": ["C2#", "D2#", "F2", "F2#", "G2#", "A2#", "C3", "C3#"],
        "Ab": ["G2#", "A2#", "C3", "C3#", "D3#", "F3", "G3", "G3#"],
        "Eb": ["D2#", "F2", "G2", "G2#", "A2#", "C3", "D3", "D3#"],
        "Bb": ["A2#", "C3", "D3", "D3#", "F3", "G3", "A3", "A3#"],
        "F": ["F2", "G2", "A2", "A2#", "C3", "D3", "E3", "F3"],
        "C": ["C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3"],
        "G": ["G2", "A2", "B2", "C3", "D3", "E3", "F3#", "G3"],
        "D": ["D2", "E2", "F2#", "G2", "A2", "B2", "C3#", "D3"],
        "A": ["A2", "B2", "C3#", "D3", "E3", "F3#", "G3#", "A3"],
        "E": ["E2", "F2#", "G2#", "A2", "B2", "C3#", "D3#", "E3"],
        "B": ["B2", "C3#", "D3#", "E3", "F3#", "G3#", "A3#", "B3"],
        "F#": ["F2#", "G2#", "A2#", "B2", "C3#", "D3#", "F3", "F3#"],
        "C#": ["C2#", "D2#", "F2", "F2#", "G2#", "A2#", "C3", "C3#"]}

# Mido key signatures
#  'Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Abm' 'Ebm' 'Bbm' 'Fm', 'Cm', 'Gm', 'Dm','Am','Em','Bm',
# 'F#m','C#m','G#m','D#m','A#m',