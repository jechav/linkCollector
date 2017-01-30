#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from fn.core import main

ROOT = "http://seriesblanco.com"

URL_TREE = ROOT+"/serie/526/supernatural-sobrenatural.html"
URL = ROOT+"/serie/526/temporada-{}/capitulo-{}/supernatural-sobrenatural.html"

main(sys.argv, ROOT, URL_TREE, URL)
