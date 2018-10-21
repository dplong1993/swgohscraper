import requests, bs4


# TODO ADD IN SHIP NAMES TO THE UNIT NAME LIST


class CharacterNameList:
    def __init__(self):
        self.__dark_side_link = 'https://swgoh.gg/characters/f/Dark%20Side/'
        self.__light_side_link = 'https://swgoh.gg/characters/f/Light%20Side/'
        self.__dark_side_names = []
        self.__light_side_names = []
        self.__dark_side_soup = self.generate_ship_html_collection(self.__dark_side_link)
        self.__light_side_soup = self.generate_ship_html_collection(self.__light_side_link)
        current_toon_tag = self.__dark_side_soup.body.nav.next_sibling.next_sibling.div.next_sibling.next_sibling.div.next_sibling \
            .next_sibling.ul.li.next_sibling.next_sibling.next_sibling.next_sibling
        while current_toon_tag.next_sibling.next_sibling is not None:
            # print(str(current_toon_tag.get('data-name-lower')))
            self.__dark_side_names.append(current_toon_tag.get('data-name-lower'))
            current_toon_tag = current_toon_tag.next_sibling
            # print(str(current_toon_tag))
            current_toon_tag = current_toon_tag.next_sibling
            # print(str(current_toon_tag))
        current_toon_tag = self.__light_side_soup.body.nav.next_sibling.next_sibling.div.next_sibling.next_sibling.div.next_sibling \
            .next_sibling.ul.li.next_sibling.next_sibling.next_sibling.next_sibling
        while current_toon_tag.next_sibling.next_sibling is not None:
            # print(str(current_toon_tag.get('data-name-lower')))
            self.__light_side_names.append(current_toon_tag.get('data-name-lower'))
            current_toon_tag = current_toon_tag.next_sibling
            # print(str(current_toon_tag))
            current_toon_tag = current_toon_tag.next_sibling
            # print(str(current_toon_tag))

    @staticmethod
    def generate_ship_html_collection(url):
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return soup

    def get_dark_side_names_list(self):
        return self.__dark_side_names

    def get_light_side_names_list(self):
        return self.__light_side_names

    def print_dark_side_names_lists(self):
        names_list = self.get_dark_side_names_list()
        for i in names_list:
            print(i)

    def print_light_side_names_lists(self):
        names_list = self.get_light_side_names_list()
        for i in names_list:
            print(i)

    def print_numbered_dark_side_names_list(self):
        names_list = self.get_dark_side_names_list()
        counter = 0
        for i in names_list:
            print(str(counter) + ": " + str(i))
            counter = counter + 1

    def print_numbered_light_side_names_list(self):
        names_list = self.get_light_side_names_list()
        counter = 0
        for i in names_list:
            print(str(counter) + ": " + str(i))
            counter = counter + 1
