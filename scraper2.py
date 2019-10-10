#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:59:12 2019

@author: drb
"""

# scraper2.py

import html5lib
from bs4 import BeautifulSoup
import requests


def main():
    
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, 'html5lib')
    print soup.title.string


main()


