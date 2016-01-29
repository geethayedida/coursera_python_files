# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:19:11 2016

@author: Geetha Yedida
"""

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()
xml = ET.fromstring(html)
lst = xml.findall('.//count')
sum = 0
print lst
#for num in range(len(lst)):
#   sum = sum + int(lst[num])
#print sum
