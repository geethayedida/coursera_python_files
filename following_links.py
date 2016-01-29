# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:51:06 2016

@author: Geetha Yedida
"""

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')

for p in range(int(position)):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tag_pos = 0
    tags = soup('a')

    for tag in tags:
        tag_pos = tag_pos + 1
        if (int(tag_pos) == int (count)):
            url =  tag.get('href', None)
            print url
    continue
print "Last URL: " + url

