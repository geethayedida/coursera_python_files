# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:38:46 2016

@author: Geetha Yedida
"""

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word = line.split()
    for w in word:
        if w in lst:
            continue
        lst.append(w)
lst.sort()
print lst






#stuff = list()
#stuff.append("book")
#stuff.append(9)
#print type(stuff)
#print stuff
#print 9 in stuff
#print "Me" not in stuff
#print stuff.sort()
#print len(stuff)
#print max(stuff)
##print sum(stuff)/len(stuff)
#abc = "Three words string"
#stuff.append(abc.split())
#for w in stuff:
#    print w

