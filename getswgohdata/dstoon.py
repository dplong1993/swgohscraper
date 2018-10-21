# This program is a class that represents a
# dark side character in SWGOH

from toon import Toon


class DsToon(Toon):
    def __init__(self, name, stars, level, gear, power):
        Toon.__init__(self, name, stars, level, gear, power)
        self.__alignment = 'dark'

    def get_alignment(self):
        return self.__alignment
