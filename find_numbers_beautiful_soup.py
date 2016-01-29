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
sum = 0
tags = soup('td')
for tag in soup.findAll('span'):
    tag_num = tag.text
    sum = sum + int(tag_num)
print sum 