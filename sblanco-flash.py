#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from fn.core import main

ROOT = "http://seriesblanco.com"

URL_TREE = ROOT+"/serie/1697/the-flash.html"
URL = ROOT+"/serie/1697/temporada-{}/capitulo-{}/the-flash.html"

main(sys.argv, ROOT, URL_TREE, URL)
