import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.chelseafc.com/en/teams/profile/cole-palmer')

print("Success Code" + str(r))

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='player-stat__value')
print(s)
#matches = s.find_all('img')

#print(matches)

#print(soup.prettify())

#print(r.content)


#<div class="player-stat__value">7</div>