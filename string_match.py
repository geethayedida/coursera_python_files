# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:16:21 2016

@author: Geetha Yedida
"""
try:
    textfile = open("sample.txt")
except:
    print "bad name"
    exit()
    
count  = 0
for line in textfile:
    line = line.rstrip()
    if not "Review" in line:
        continue
    count = count + 1    
    print line + " "+str(count)

