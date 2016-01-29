# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:24:35 2016

@author: Geetha Yedida
"""

import urllib
from BeautifulSoup import *

url = raw_input('Enter -')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    print tag.get('href',None)