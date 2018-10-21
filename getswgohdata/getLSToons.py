import requests, bs4

def getLSToons(memberLink):
    res = requests.get('https://swgoh.gg/' + memberLink + 'collection')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    characterList_tag = soup.body.nav.next_sibling.next_sibling.div.next_sibling.next_sibling.div.next_sibling.next_sibling.ul.li.next_sibling.next_sibling.next_sibling.next_sibling.div
    characters = [ ]
    counter = characterList_tag.div
    while(counter != None):
        characters.append(counter)
        counter = counter.next_sibling.next_sibling
    #The list characters now contains the html object for each character in member's collection.

    lightSideCharacters = []
    counter = characterList_tag.div
    while(counter != None):
        atributes = counter.div['class']
        if('light' in str(atributes[1])):
            lightSideCharacters.append(counter.div)
            counter = counter.next_sibling.next_sibling
        else:
            counter = counter.next_sibling.next_sibling

    lightSideNames = []
    for i in range(len(lightSideCharacters)):
        lightSideNames.append(str(lightSideCharacters[i].img['alt']))

    lightSideStars = []
    for i in range(len(lightSideCharacters)):
        star_tag = lightSideCharacters[i].img.next_sibling.next_sibling
        star_count = 0
        for j in range(7):
            star_tag = star_tag.next_sibling.next_sibling
            if(len(star_tag.get('class')) == 2):
                star_count += 1
        lightSideStars.append(star_count)

    lightSideToons = {}
    for i in range(len(lightSideCharacters)):
        lightSideToons.setdefault(lightSideNames[i], lightSideStars[i])

    return lightSideToons
