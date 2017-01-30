#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup as Soup
from termcolor import colored
import requests

def getUrl(URL, ROOT, LENGUAGUE, SERVER):
    tmpURLS = []
    tt = requests.get(URL)
    soup = Soup(tt.content,  'html.parser')
    trs = soup.find('table', {'class': 'table-Hover'}).find_all('tr')
    for ind, t in enumerate(trs):
        tds = t.find_all('td')
        img = tds[1].find('img')
        img2 = tds[2].find('img')
        if img and img2:
            if img.get('src') == LENGUAGUE and img2.get('src') == SERVER:
                tmpURLS.append( ROOT+tds[2].find('a').get('href') )

    for ind, url in enumerate(tmpURLS):
        vUrl =  _getUrl2(url)
        av = _checkUp(vUrl)
        print(colored(vUrl, 'green' if av else 'red'))

def _getUrl2(url):
    tt = requests.get(url)
    soup = Soup(tt.content,  'html.parser')
    btn = soup.find('input', {'type': 'button'})
    enlace = btn.get('onclick')
    # print(enlace)
    return enlace.split('"')[1]

def _checkUp(url):
    tt = requests.get(url)
    soup = Soup(tt.content,  'html.parser')
    return soup.find('video') != None

def tree(URLTREE):
    tt = requests.get(URLTREE)
    soup = Soup(tt.content,  'html.parser')
    seasons = soup.findAll('div', {'class': 'panel-collapse'})
    chapters = soup.findAll('tr', {'class': 'table-hover'})

    print(colored('Temporadas {} - Capitulos {}'.format(len(seasons), len(chapters)), 'green'))

    for ind, s in enumerate(seasons):
        links = _getChapters(ind+1, chapters)
        print(colored('Temporada {} - {}'.format(ind+1, len(links)), 'blue'))

def _getChapters(s, chapters):
    n = [];
    for ind, c in enumerate(chapters):
        if c.text.strip().split('x')[0] == str(s):
            n.append(c.find('a').get('href'))
    return n
