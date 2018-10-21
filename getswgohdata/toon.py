# This program is a class that represents a
# unit in SWGOH.


class Toon:
    def __init__(self, name, stars, level, gear, power):
        self.__name = name
        self.__stars = stars
        self.__power = power
        self.__level = level
        self.__gear = gear

    def get_name(self):
        return self.__name

    def print_name(self):
        print(self.__name)

    def get_power(self):
        return self.__power

    def print_power(self):
        print(self.__power)

    def get_stars(self):
        return self.__stars

    def print_stars(self):
        print(self.__stars)

    def get_gear_level(self):
        return self.__gear

    def print_gear_level(self):
        print(str(self.__gear))

    def get_unit_level(self):
        return self.__level

    def print_unit_level(self):
        print(str(self.__level))

    def print_unit(self):
        return self.__name + ' ' + str(self.__stars)

    def __eq__(self, other):
        if self.__name == other:
            return True
        else:
            return False
