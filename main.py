#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from fn.core import main

ROOT = "http://seriesblanco.com"

URL_TREE = ROOT+"/serie/1697/the-flash.html"
URL = ROOT+"/serie/1697/temporada-{}/capitulo-{}/the-flash.html"

URL_TREE = ROOT+"/serie/1653/rick-and-morty.html"
URL = ROOT+"/serie/1653/temporada-{}/capitulo-{}/rick-and-morty.html"

URL_TREE = ROOT+"/serie/526/supernatural-sobrenatural.html"
URL = ROOT+"/serie/526/temporada-{}/capitulo-{}/supernatural-sobrenatural.html"

URL_TREE = ROOT+"/serie/1531/black_sails.html"
URL = ROOT+"/serie/1531/temporada-{}/capitulo-{}/black_sails.html"


main(sys.argv, ROOT, URL_TREE, URL)
