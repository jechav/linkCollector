#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup as Soup
from termcolor import colored
import requests

import sys, pprint
pp = pprint.PrettyPrinter(indent=4)

if len(sys.argv) < 3:
    print(colored('Usage ', 'white'))
    print(colored('python main.py [season] [chapter] [lenguague = sub] [server = openload]', 'white'))
    print(colored('lenguague: sub, lat, es', 'white'))
    print(colored('servers: openload, flashx, streamin, nowvideo', 'white'))
    sys.exit()

ROOT = "http://seriesblanco.com"
URL = ROOT+"/serie/1697/temporada-{}/capitulo-{}/the-flash.html".format(sys.argv[1], sys.argv[2])

class flags:
    sub = 'http://seriesblanco.com/banderas/vos.png'
    lat = 'http://seriesblanco.com/banderas/la.png'
    es = 'http://seriesblanco.com/banderas/es.png'

class servers:
    openload = '/servidores/openload.png'
    flashx = '/servidores/flashx.jpg'
    streamin = '/servidores/streamin.to.jpg'
    nowvideo = '/servidores/nowvideo.png'

LENGUAGUE = getattr(flags, sys.argv[3]) if len(sys.argv) > 3 else flags.sub
SERVER = getattr(servers, sys.argv[4]) if len(sys.argv) > 4 else servers.openload

print( colored(URL, 'blue') )
print( colored(LENGUAGUE+' - '+SERVER, 'white') )

def main():
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
                # print( tds[2].find('a').get('href') )

    for ind, url in enumerate(tmpURLS):
        vUrl =  getUrl2(url)
        av = checkUp(vUrl)
        print(colored(vUrl, 'green' if av else 'red'))

def getUrl2(url):
    tt = requests.get(url)
    soup = Soup(tt.content,  'html.parser')
    btn = soup.find('input', {'type': 'button'})
    enlace = btn.get('onclick')
    # print(enlace)
    return enlace.split('"')[1]

def checkUp(url):
    tt = requests.get(url)
    soup = Soup(tt.content,  'html.parser')
    return soup.find('video') != None


main()

