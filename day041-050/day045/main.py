import os
import sys
from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://www.empireonline.com/movies/features/best-movies-2/')
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
titles = [f"{title_tag.text}\n" for title_tag in soup.select(
    selector="div.gallery section h3.title")]
titles.reverse()

with open(os.path.join(sys.path[0], 'movies.txt'), 'w') as file:
    file.writelines(titles)
