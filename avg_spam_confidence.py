# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:12:26 2016

@author: Geetha Yedida
"""

fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'bad file'
    exit()
count = 0
sc = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    sc = sc + float(line[23:29])
avg = sc/count
print "Average spam confidence: " + str(avg)