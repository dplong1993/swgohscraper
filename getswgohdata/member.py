# This program is a class that represents
# a person in a guild in SWGOH

import requests, bs4, lstoon, dstoon, ship


class Member:

    def __init__(self, name, url):

        self.__name = name
        self.__url = url
        self.__totalGP = 0
        self.__charGP = 0
        self.__shipGP = 0
        self.__dstoons = []
        self.__lstoons = []
        self.__ships = []

        # Use url to access member's html on SWGOH.GG
        self.__soup = self.generate_html_collection(self.__name, self.__url)

        # Search html for all the member's toons
        self.__lstoons, self.__dstoons = self.generate_character_lists(self.__soup, self.__lstoons, self.__dstoons)

        # Use url to get member's ships
        self.__soup = self.generate_ship_html_collection(self.__url)
        self.__ships = self.generate_ship_list(self.__soup, self.__ships)

        # Use url to generate Member's total gp, char gp, and ship gp
        self.__soup = self.generate_gal_pow_html(self.__url)
        self.__totalGP = self.generate_total_gal_pow(self.__soup)
        self.__charGP = self.generate_char_gal_pow(self.__soup)
        self.__shipGP = self.generate_ship_gal_pow(self.__soup)

    # Use url to access member's collection in html on SWGOH.GG
    @staticmethod
    def generate_html_collection(name, url):
        print("Getting " + name + "'s data.")
        res = requests.get('https://swgoh.gg/' + url + 'collection')
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return soup

    # Search html for to generate lists of the member's dark side and light side characters.
    @staticmethod
    def generate_character_lists(soup, lstoons, dstoons):
        character_list_tag = soup.body.nav.next_sibling.next_sibling.div \
            .next_sibling.next_sibling.div.next_sibling \
            .next_sibling.ul.li.next_sibling.next_sibling \
            .next_sibling.next_sibling.div

        current_toon = character_list_tag.div
        # print("CURRENT TOON IS " + str(current_toon))
        while current_toon is not None:
            alignment = current_toon.div['class']
            # print("ALIGNMENT IS " + str(alignment))
            if 'light' in str(alignment[1]):
                name = current_toon.div.img['alt']
                # print("Adding " + name + " to " + self.__name + "'s collection")
                star_tag = current_toon.div.img.next_sibling.next_sibling
                # print("STAR TAG IS " + str(star_tag))
                stars = 0
                for i in range(7):
                    star_tag = star_tag.next_sibling.next_sibling
                    if len(star_tag.get('class')) == 2:
                        stars += 1
                level_tag = star_tag.next_sibling.next_sibling
                # print("LEVEL TAG IS " + str(level_tag))
                level = level_tag.get_text()
                # print("LEVEL IS " + str(level))
                gear_tag = level_tag.next_sibling.next_sibling
                # print("GEAR TAG IS " + str(gear_tag))
                gear = gear_tag.get_text()
                # print("GEAR IS " + str(gear))
                power_tag = current_toon.div.div.next_sibling.next_sibling
                # print("POWER TAG IS " + str(power_tag))
                power_str = power_tag.get('title')
                # print("POWER IS " + str(power_str))
                a, power, c, d = power_str.split(' ')
                # print("POWER IS " + str(power))
                new_ls_toon = lstoon.LsToon(name, stars, level, gear, power)
                lstoons.append(new_ls_toon)
            elif 'dark' in str(alignment[1]):
                name = current_toon.div.img['alt']
                # print("Adding " + name + " to " + self.__name + "'s collection")
                star_tag = current_toon.div.img.next_sibling.next_sibling
                stars = 0
                for i in range(7):
                    star_tag = star_tag.next_sibling.next_sibling
                    if len(star_tag.get('class')) == 2:
                        stars += 1
                level_tag = star_tag.next_sibling.next_sibling
                level = level_tag.get_text()
                gear_tag = level_tag.next_sibling.next_sibling
                gear = gear_tag.get_text()
                power_tag = current_toon.div.div.next_sibling.next_sibling
                power_str = power_tag.get('title')
                a, power, c, d = power_str.split(' ')
                new_ds_toon = dstoon.DsToon(name, stars, level, gear, power)
                dstoons.append(new_ds_toon)
            else:
                print("Uhoh something messed up when trying to get this toon.")
            current_toon = current_toon.next_sibling.next_sibling
        return lstoons, dstoons

    # Use url to get html soup that contains the member's ships.
    @staticmethod
    def generate_ship_html_collection(url):
        url = 'https://swgoh.gg/' + url + 'ships'
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return soup

    # Search html to generate a list of the member's ship.
    @staticmethod
    def generate_ship_list(soup, ship_list):
        ship_list_tag = soup.body.nav.next_sibling.next_sibling.div \
            .next_sibling.next_sibling.div.next_sibling \
            .next_sibling.ul.li.next_sibling.next_sibling \
            .next_sibling.next_sibling.div
        current_ship = ship_list_tag.div
        # print(str(current_ship))
        while current_ship is not None:
            # print("NEXT SHIP")
            name = current_ship.img['alt']
            # print(str(name))
            power_tag = current_ship.div.div.div.next_sibling.next_sibling.div
            # Sprint(str(power_tag))
            power_str = power_tag.get('title')
            # print(power_str)
            if 'collection-char-gp' in power_tag.get('class'):
                a, power, c, d = power_str.split(' ')
                level_tag = current_ship.a.div.next_sibling.next_sibling.div \
                    .next_sibling.next_sibling.next_sibling.next_sibling
                level = level_tag.get_text()
            else:
                power = 0
                level = 0
            star_tag = current_ship.a.div.div
            stars = 0
            for i in range(7):
                next_sibling = star_tag.find_next_sibling()
                if next_sibling is None and i != 6:
                    stars = 0
                    break
                if 'ship-portrait-full-star-inactive' not in star_tag.get('class'):
                    stars += 1
                star_tag = star_tag.next_sibling.next_sibling
            new_ship = ship.Ship(name, stars, level, power)
            ship_list.append(new_ship)
            current_ship = current_ship.next_sibling.next_sibling
        return ship_list

    # Use url to generate a html soup that contains the member's galactic power values.
    @staticmethod
    def generate_gal_pow_html(url):
        res = requests.get("https://swgoh.gg/" + url)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        return soup

    # Search html for member's total galactic power.
    @staticmethod
    def generate_total_gal_pow(soup):
        total_gp_tag = soup.body.nav.next_sibling.next_sibling.div.next_sibling \
            .next_sibling.div.div.next_sibling.next_sibling.next_sibling \
            .next_sibling.next_sibling.next_sibling.div.div.p
        x = total_gp_tag.get_text()
        a, b, c = x.split(" ")
        c = c.replace(',', '')
        return int(c)

    # Search html for member's character galactic power.
    @staticmethod
    def generate_char_gal_pow(soup):
        char_gp_tag = soup.body.nav.next_sibling.next_sibling.div.next_sibling \
            .next_sibling.div.div.next_sibling.next_sibling.next_sibling \
            .next_sibling.next_sibling.next_sibling.div.div.p.next_sibling \
            .next_sibling
        x = char_gp_tag.get_text()
        a, b, c, d = x.split(" ")
        d = d.replace(',', '')
        return int(d)

    # Search html for member's ship galactic power.
    @staticmethod
    def generate_ship_gal_pow(soup):
        ship_gp_tag = soup.body.nav.next_sibling.next_sibling.div.next_sibling \
            .next_sibling.div.div.next_sibling.next_sibling.next_sibling \
            .next_sibling.next_sibling.next_sibling.div.div.p.next_sibling \
            .next_sibling.next_sibling.next_sibling
        x = ship_gp_tag.get_text()
        a, b, c, d = x.split(" ")
        d = d.replace(',', '')
        return int(d)

    # Returns the name of the member.
    def get_name(self):
        return self.__name

    # Returns the url of the member.
    def get_url(self):
        return self.__url

    # Returns the member's list of dark side characters.
    def get_dstoons(self):
        return self.__dstoons

    # Returns the member's list of light side characters.
    def get_lstoons(self):
        return self.__lstoons

    # Returns the member's list of ships
    def get_ships(self):
        return self.__ships

    # RETURNS A LIST OF THE NAMES OF ALL OF A MEMBERS CHARACTERS AND SHIPS. (DONE)
    def get_list_of_ships_and_characters(self):
        object_list = self.get_lstoons()
        new_list = []
        for i in object_list:
            new_list.append(i.get_name())
        object_list = self.get_dstoons()
        for i in object_list:
            new_list.append(i.get_name())
        object_list = self.get_ships()
        for i in object_list:
            new_list.append(i.get_name())
        return new_list

    # PRINTS A LIST OF THE NAMES OF ALL OF A MEMBERS CHARACTERS AND SHIPS. (DONE)
    def print_list_of_ships_and_characters(self):
        object_list = self.get_lstoons()
        new_list = []
        for i in object_list:
            new_list.append(i.get_name())
        object_list = self.get_dstoons()
        for i in object_list:
            new_list.append(i.get_name())
        object_list = self.get_ships()
        for i in object_list:
            new_list.append(i.get_name())
        for i in new_list:
            print(i)
        return

    # TODO Return a dictionary that contains the name of the member's light side characters and the int
    # TODO value of those characters' stars.

    # TODO Return a dictionary that contains the name of the member's dark side characters and the int
    # TODO value of those characters' stars.

    # TODO Return a dictionary that contains the name of the member's ships and the int
    # TODO value of those ships' stars.

    # TODO Print the name of the member's light side characters and the int value of those characters' stars.

    # TODO Print the name of the member's dark side characters and the int value of those characters' stars.

    # TODO Print the name of the member's ships and the int value of those ships' stars.

    # TODO Print the name of the member's ships, light side characters, and dark side
    # TODO characters and the star values for each.

    # Return the star level for a character or ship based on a name that is provided. If that name is not found 0 is
    # returned.
    def get_star_level(self, name):
        toon_list = self.__dstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_stars()
        toon_list = self.__lstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_stars()
        toon_list = self.__ships
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_stars()
        # print("Name not found in dstoon, lstoon, or ship collections of " + str(self.get_name()) + ". Returning 0.")
        return 0

    # Return the gear level for a character based on a name that is provided. If that name is not found 0 is
    # returned.
    def get_gear_level(self, name):
        toon_list = self.__dstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_gear_level()
        toon_list = self.__lstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_gear_level()
        # print("Name not found in dstoon, lstoon, or ship collections of " + str(self.get_name()) + ". Returning 0.")
        return 0

    # Return the level for a character or ship based on a name that is provided. If that name is not found 0 is
    # returned.
    def get_unit_levels(self, name):
        toon_list = self.__dstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_unit_level()
        toon_list = self.__lstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_unit_level()
        toon_list = self.__ships
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_unit_level()
        # print("Name not found in dstoon, lstoon, or ship collections of " + str(self.get_name()) + ". Returning 0.")
        return 0

    # Return the power for a character or ship based on a name that is provided. If that name is not found 0 is
    # returned.
    def get_toon_power(self, name):
        toon_list = self.__dstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_power()
        toon_list = self.__lstoons
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_power()
        toon_list = self.__ships
        for i in toon_list:
            if name == i.get_name().lower():
                return i.get_power()
        # print("Name not found in dstoon, lstoon, or ship collections of " + str(self.get_name()) + ". Returning 0.")
        return 0

    # Return the member's total GP aka Character GP plus Ship GP
    def get_total_gp(self):
        return self.__totalGP

    # Print the member's total GP aka Character GP plus Ship GP
    def print_total_gp(self):
        print(str(self.__totalGP))

    # Return the member's total character GP
    def get_char_gp(self):
        return self.__charGP

    # Print the member's total character GP
    def print_char_gp(self):
        print(str(self.__charGP))

    # Return the member's total ship GP
    def get_ships_gp(self):
        return self.__shipGP

    # Print the member's total ship GP
    def print_ships_gp(self):
        print(str(self.__shipGP))

    # TODO UNFINISHED FUNCTIONS
    def get_member_toon_roster(self):
        # TODO CHANGE WIDTH TO 40 OR 45 B/C OF SHIPS
        # WIDTH CURRENTLY AT 35
        print("Dark Side Toons" + '{:>20}'.format('**'))
        print(35 * "*")
        for i in self.__dstoons:
            print('{:33}'.format(i.print_toon()) + '**')
        print(35 * "*")
        print("Light Side Toons" + '{:>19}'.format('**'))
        print(35 * "*")
        for i in self.__lstoons:
            print('{:33}'.format(i.print_toon()) + '**')
        print(35 * "*")
        print("Ships" + '{:>30}'.format('**'))
        print(35 * "*")
        for i in self.__ships:
            print('{:33}'.format(i.print_toon()) + '**')
        print(35 * "*")

    def get_count_of_character(self, name, stars, alignment):
        if alignment == 'light':
            for i in self.__lstoons:
                if i == name:
                    # print(self.__name)
                    if i.get_stars() >= stars:
                        print(self.__name)
                        return 1
                    return 0
        elif alignment == 'dark':
            for i in self.__dstoons:
                if i == name:
                    if i.get_stars() >= stars:
                        return 1
                    return 0
        else:
            for i in self.__ships:
                if i == name:
                    if i.get_stars() >= stars:
                        return 1
                    return 0
        return 0

    def __str__(self):
        return self.__name + " " + self.__url + " " + str(self.__totalGP) + " " + str(self.__charGP) + " " + str(
            self.__shipGP)
