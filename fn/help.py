#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup as Soup
from termcolor import colored
import requests

def getUrl(URL, ROOT, LENGUAGUE, SERVER):
    tmpURLS = []
    tt = _REQUEST(URL)
    if not tt: return False
    soup = Soup(tt.content,  'html.parser')
    trs = soup.find('table', {'class': 'table-Hover'}).find_all('tr')
    if LENGUAGUE == 'all':
        return _deepGet(ROOT, trs)

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

    if(len(tmpURLS) < 1): _deepGet(ROOT, trs) # call deepget if no result for lenguague and serv

def _deepGet(ROOT, trs):
    flag = None
    for ind, t in enumerate(trs):
        tds = t.find_all('td')
        img = tds[1].find('img')
        img2 = tds[2].find('img')
        if img and img2:
            if flag <> img.get('src'):
                flag = img.get('src')
                print(colored(flag, 'cyan'))

            url = ROOT+tds[2].find('a').get('href')
            vUrl =  _getUrl2(url)
            av = _checkUp(vUrl)
            print(colored(vUrl, 'green' if av else 'red'))





def _getUrl2(url):
    tt = _REQUEST(url)
    if not tt: return False
    soup = Soup(tt.content,  'html.parser')
    btn = soup.find('input', {'type': 'button'})
    enlace = btn.get('onclick')
    # print(enlace)
    return enlace.split('"')[1]

def _checkUp(url):
    tt = _REQUEST(url);
    if not tt: return False
    soup = Soup(tt.content,  'html.parser')
    return soup.find('video') != None

def tree(URLTREE):
    tt = _REQUEST(URLTREE)
    if not tt: return False
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

def _REQUEST(url):
    try:
        return requests.get(url)
    except requests.exceptions.Timeout:
        print(colored('Timeout', 'red'))
    except requests.exceptions.TooManyRedirects:
        print(colored('TooManyRedirects', 'red'))
    except requests.exceptions.RequestException as e:
        print(colored('RequestException', 'red'))

    return False;
