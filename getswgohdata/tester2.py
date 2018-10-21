import guild


def main():
    url = 'https://swgoh.gg/g/45150/tens-hbc-the-sitherins/'
    one = guild.Guild(url)
    one.write_member_rosters_to_spreadsheet()


main()
