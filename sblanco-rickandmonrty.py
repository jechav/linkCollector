#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from fn.core import main

ROOT = "http://seriesblanco.com"

URL_TREE = ROOT+"/serie/1653/rick-and-morty.html"
URL = ROOT+"/serie/1653/temporada-{}/capitulo-{}/rick-and-morty.html"

main(sys.argv, ROOT, URL_TREE, URL)
