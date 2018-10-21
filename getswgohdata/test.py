import guild
import completeNameRosterForToons


def main():
    url = 'https://swgoh.gg/g/4504/imperial-palace-guard/'
    # url = 'https://swgoh.gg/g/33944/ten-delusions-of-grandeur/'
    # url = 'https://swgoh.gg/g/45150/tens-hbc-the-sitherins/'
    # one = guild.Guild(url)
    item = completeNameRosterForToons.CharacterNameList()
    item.print_numbered_dark_side_names_list()
    item.print_numbered_light_side_names_list()


main()
