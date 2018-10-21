import requests, bs4

def getNames(guildLink):
    res = requests.get(guildLink)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    member_tag = soup.body.table.tbody.tr    #This takes us to the first member of the guild

    names = []

    while(member_tag != None):
        name = str(member_tag.a.strong.string)
        names.append(name)
        member_tag = member_tag.next_sibling.next_sibling

    return names
    
def getLinks(guildLink):
    res = requests.get(guildLink)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    member_tag = soup.body.table.tbody.tr    #This takes us to the first member of the guild

    links = []

    while(member_tag != None):
        link = member_tag.a.get('href')
        links.append(link)
        member_tag = member_tag.next_sibling.next_sibling

    return links
