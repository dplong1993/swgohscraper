#!/usr/bin/python3
###########################################################################
#This is a the main program used to collect light side and dark side characters for specific
# a specific guild
###########################################################################

import getMembers
import getLSToons
import getDSToons
import getShips
import writeLightToons
import writeDarkToons
import writeShips

def main():
    guildLink = 'https://swgoh.gg/g/4504/imperial-palace-guard/'
    memberLSToons = {}
    memberDSToons = {}
    memberShips = {}
    memberNames = []
    memberLinks = []

    #Gets the names and links to the members of the guild.
    print("Getting names and links")
    memberNames = getMembers.getNames(guildLink)
    memberLinks = getMembers.getLinks(guildLink)

    #Add's the member's light side and dark side toons and ships to dictionaries
    print("Getting toons")
    for i in range(len(memberLinks)):
        print("Getting " + memberNames[i] + " light side toons.")
        memberLSToons.setdefault(memberNames[i], getLSToons.getLSToons(memberLinks[i]))
        print("Getting " + memberNames[i] + " dark side toons.")
        memberDSToons.setdefault(memberNames[i], getDSToons.getDSToons(memberLinks[i]))
        print("Getting " + memberNames[i] + " ships.")
        memberShips.setdefault(memberNames[i], getShips.scrapeData(memberLinks[i]))
        print("Starting on next member")

    #Open a text file to write the data to.
    newFile = open('test.txt', 'w')
    print("Writing light side toons")
    newFile.write("\nLIGHT    SIDE     TOONS\n")

    #Write out all the light side toons
    for k, v in memberLSToons.items():
        newFile.write(str(k) + '\n')
        for i, j in v.items():
            newFile.write(str(i) + ': ' + str(j) + '\n')
        newFile.write('\n\n\n')

    print("Writing dark side toons")
    newFile.write("\nDARK     SIDE      TOONS\n")

    #Write out all the dark side toons
    for k, v in memberDSToons.items():
        newFile.write(str(k) + '\n')
        for i, j in v.items():
            newFile.write(str(i) + ': ' + str(j) + '\n')
        newFile.write('\n\n\n')

    print("Writing ships")
    newFile.write("\n       SHIPS           \n")

    #Write out all the ships
    for k, v in memberShips.items():
        newFile.write(str(k) + '\n')
        for i, j in v.items():
            newFile.write(str(i) + ': ' + str(j) + '\n')
        newFile.write('\n\n\n')

    newFile.close()

    writeLightToons.write(memberNames, memberLSToons)
    writeDarkToons.write(memberNames, memberDSToons)
    writeShips.write(memberNames, memberShips)

    


main()
