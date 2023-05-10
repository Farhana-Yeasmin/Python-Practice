from bs4 import BeautifulSoup
import requests
import re

# website = "https://subslikescript.com/movies"
root = "https://subslikescript.com"
website = f'{root}/movies'

response = requests.get(website)
content = response.text
# print(content)

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')
# print(box)

# All the movie names in a list
movie_name = box.find_all('li')

# to get the movie name iterate it and get text
# for name in movie_name:
#     name = name.get_text()
#     name = re.sub(r'\(\d+\)', '', name).strip()
#     print(name)


links = []
for link in box.find_all('a', href=True):
    """
    with Regex capture the link
    """
    url = re.findall(r'href="(.+?)"', str(link))
    url = url[0]
    """
    without Regex capture the link
    """
    # print(link['href'])
    links.append(url)

for link in links:
    try:
        website = f'{root}/{link}'
        response = requests.get(website)
        content = response.text
        # print(content)

        soup = BeautifulSoup(content, 'lxml')
        # print(soup.prettify())

        box = soup.find('article', class_='main-article')
        tittle = box.find('h1').get_text()
        transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

        with open(f'{tittle}.txt', 'w') as file:
            file.write(transcript)
    except:
        print('------ Link not working -------')
        print(link)
