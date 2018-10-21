# This program is a class that represents a
# light side character in SWGOH

from toon import Toon


class LsToon(Toon):
    def __init__(self, name, stars, level, gear, power):
        Toon.__init__(self, name, stars, level, gear, power)
        self.__alignment = 'light'

    def get_alignment(self):
        return self.__alignment
