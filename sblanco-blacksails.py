#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from fn.core import main

ROOT = "http://seriesblanco.com"

URL_TREE = ROOT+"/serie/1531/black_sails.html"
URL = ROOT+"/serie/1531/temporada-{}/capitulo-{}/black_sails.html"


main(sys.argv, ROOT, URL_TREE, URL)
