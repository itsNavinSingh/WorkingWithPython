import bs4
import requests

response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2')
soup = bs4.BeautifulSoup(response.text, 'html.parser')
article = soup.find_all(name='h3', class_='title')
assending_list = []

for i in range (len(article)-1, -1, -1):
    name = article[i].string
    assending_list.append(name)

with open('top_movie.txt', mode='a', encoding='utf-8') as txt100:
    for movie in assending_list:
        txt100.write(f'{movie}\n')