from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')

tittle = box.find('h1').get_text()

transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# print(tittle)
# print(transcript)
# write txt file
with open(f'{tittle}.tx t', 'w') as file:
    file.write(transcript)