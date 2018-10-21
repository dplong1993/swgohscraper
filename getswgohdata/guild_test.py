#This program is used to test the Guild class

import guild

def main():
    my_guild = guild.Guild('https://swgoh.gg/g/45150/tens-heroicbootcamp/')
    count = my_guild.get_count_of_character('Ghost', 3, 'ship')
    print(count)
main()

