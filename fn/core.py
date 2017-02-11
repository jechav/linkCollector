#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, getopt
from termcolor import colored

from var import flags, servers
from help import getUrl, tree

def main(argv, ROOT, URL_TREE, URL):
    # print(len(argv))
    if len(argv) > 1 and argv[1] == 'tree':
        print( colored(URL_TREE, 'blue') )
        tree(URL_TREE)
        sys.exit()


    if len(argv) < 3:
        error()

    if len(argv) == 4 and sys.argv[3] == 'all':
        LENGUAGUE = 'all'
        SERVER = 'all'
    else:
        try:
            LENGUAGUE = getattr(flags, sys.argv[3]) if len(sys.argv) > 3 else flags.sub
            SERVER = getattr(servers, sys.argv[4]) if len(sys.argv) > 4 else servers.openload
        except:
            error()


    URL = URL.format(sys.argv[1], sys.argv[2]) # set season and champter


    print( colored(URL, 'blue') )
    print( colored(LENGUAGUE+' - '+SERVER, 'white') )
    getUrl(URL, ROOT, LENGUAGUE, SERVER)

def error():
    print('Usage:  ')
    print(colored('tree', 'white'))
    print(colored('[season] [chapter] [lenguague = sub] [server = openload]', 'white'))
    print(colored('[season] [chapter] all', 'white'))
    print('lenguague: sub, lat, es')
    print('servers: openload, streamin, streamplay, flashx, nowvideo')
    sys.exit(2)





