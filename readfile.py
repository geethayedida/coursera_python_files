# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:43:09 2016

@author: Geetha Yedida
"""

textfile = open("sample.txt")
count  = 0
for line in textfile:
    line = line.rstrip()
    if not line.startswith("Review"):
        continue
    count = count +1
print count