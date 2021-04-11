BEATS_P_MEASURE = 4.0
MEASURES_P_MELODY = 4
KEY = "C"
TEMPO = 90 # BPM
NOTE_RANGE = ["C4", "C4#", "D4", "D4#", "E4", "F4", "F4#", "G4", "G4#", "A4", "A4#", "B4", "C5", 
            "C5#", "D5", "D5#", "E5", "F5", "F5#", "G5", "G5#", "A5", "A5#", "B5", 'C6',
            "Rest", "Rest", "Rest", "Rest"]

NOTE_TO_MIDI = {'C4': 60, 'C4#': 61, 'D4': 62, 'D4#': 63, 'E4': 64, 'F4': 65, 'F4#': 66, 'G4': 67, 
                'G4#': 68, 'A4': 69, 'A4#': 70, 'B4': 71, 'C5': 72, 'C5#': 73, 'D5': 74, 'D5#': 75, 
                'E5': 76, 'F5': 77, 'F5#': 78, 'G5': 79, 'G5#': 80, 'A5': 81, 'A5#': 82, 'B5': 83, 
                'C6': 84, 'Rest': 128}

MIDI_TO_NOTE = {60: 'C4', 61: 'C4#', 62: 'D4', 63: 'D4#', 64: 'E4', 65: 'F4', 66: 'F4#', 67: 'G4', 
                68: 'G4#', 69: 'A4', 70: 'A4#', 71: 'B4', 72: 'C5', 73: 'C5#', 74: 'D5', 75: 'D5#', 
                76: 'E5', 77: 'F5', 78: 'F5#', 79: 'G5', 80: 'G5#', 81: 'A5', 82: 'A5#', 83: 'B5', 
                84: 'C6', 128: 'Rest'}

BEAT_VALUES = [2.0, 1.0, 0.5, 0.25] # Note: Whole notes have been removed for now

VELOCITY_RANGE = [53, 64, 80, 96] # MP, MF, F, FF