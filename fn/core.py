#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, getopt
from termcolor import colored

from var import flags, servers
from help import getUrl, tree

def main(argv, ROOT, URL_TREE, URL):
    if len(argv) > 1 and argv[1] == 'tree':
        print( colored(URL_TREE, 'blue') )
        tree(URL_TREE)
        sys.exit()


    if len(argv) < 3:
        print('Usage:  ')
        print(colored('tree', 'white'))
        print(colored('[season] [chapter] [lenguague = sub] [server = openload]', 'white'))
        print('lenguague: sub, lat, es')
        print('servers: openload, flashx, streamin, nowvideo')
        sys.exit(2)

    LENGUAGUE = getattr(flags, sys.argv[3]) if len(sys.argv) > 3 else flags.sub
    SERVER = getattr(servers, sys.argv[4]) if len(sys.argv) > 4 else servers.openload
    URL = URL.format(sys.argv[1], sys.argv[2]) # set season and champter

    print( colored(URL, 'blue') )
    print( colored(LENGUAGUE+' - '+SERVER, 'white') )
    getUrl(URL, ROOT, LENGUAGUE, SERVER)





