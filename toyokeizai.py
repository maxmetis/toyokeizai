# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:41:27 2020

@author: Johnny Tsai
"""

import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

def toyokeizai_news():
    url = 'https://toyokeizai.net'

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('ul')[5]

    title = [title_item.text for title_item in data.find_all('span', class_='column-main-ttl')]
    link = [url + link_item.get('href') for link_item in data.find_all('a')]
    img = [img_item.get('srcset').split(',')[1].replace(' 2x','') for img_item in data.find_all('img')]

    return title, link, img

print(toyokeizai_news())




