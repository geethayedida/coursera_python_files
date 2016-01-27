# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:00:12 2016

@author: Geetha Yedida
"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        sub = line.split()
        print sub[1]
        count = count + 1
print "There were " +str(count)+ " lines in the file with From as the first word"
