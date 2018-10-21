# This is a temporary program that is being used
# to determine how to scrape ship data from swgoh.gg

import requests, bs4
import getShips

def main():
    url = 'u/dplong/'
    ships = getShips.scrapeData(url)
    for i, j in ships.items():
        print(str(i) + ': ' + str(j))


############################################################
main()
