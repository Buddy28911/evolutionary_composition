class John:
    def __init__(self, vibe):
        self.num = 4
        self.num2 = self.num2func(vibe)
        return

    def num2func(self, vibe):
        return 5+vibe

jj = John(4)


from representation import Melody

import mido
from mido import MidiFile
