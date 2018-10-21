# This program is a class that represents a
# ship in SWGOH

from toon import Toon


class Ship(Toon):
    def __init__(self, name, stars, level, power):
        Toon.__init__(self, name, stars, level, 'X', power)
        self.__alignment = 'ship'

    def get_alignment(self):
        return self.__alignment
