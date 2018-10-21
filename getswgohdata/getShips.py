import requests, bs4

def scrapeData(memberLink):
    res = requests.get('https://swgoh.gg/' + memberLink + 'ships')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    shipList_tag = soup.body.nav.next_sibling.next_sibling.div\
                            .next_sibling.next_sibling.div.next_sibling\
                            .next_sibling.ul.li.next_sibling.next_sibling\
                            .next_sibling.next_sibling.div
    current_ship = shipList_tag.div

    ships = {}
    
    while(current_ship != None):
        name = current_ship.img['alt']
        star_tag = current_ship.a.div.div
        stars = 0
        for i in range(7):
            next_sibling = star_tag.find_next_sibling()
            if(next_sibling is None and i != 6):
                stars = 0
                break
            if('ship-portrait-full-star-inactive' not in star_tag.get('class')):
                stars += 1
            star_tag = star_tag.next_sibling.next_sibling
        ships.setdefault(name, stars)
        current_ship = current_ship.next_sibling.next_sibling

    return ships

    
