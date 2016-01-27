# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:01:31 2016

@author: Geetha Yedida
"""

fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'bad file'
    exit()
for line in fh:
    line = line.rstrip()
    print line.upper()
