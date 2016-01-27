# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:10:06 2016

@author: Geetha Yedida
"""

import re
fl = open(raw_input("Enter file name: "))
sum = 0
for line in fl:
    line = line.rstrip()
    num= re.findall('[0-9]+',line)
    for i in num:
        sum = sum + int(i)
print sum

#fl = open(raw_input("Enter file name: "))
#for line in fl:
#    line = line.rstrip()
#    if re.search("^F.+: ",line): #Greedy matching: picks the biggest strings if there are multiple :'s
#        #from at the beginning of line
#        print line
## numbers with one digit or more        
#x = "Python turned out 2 be the best 1 course out of 20 best courses stephen@uct.ac.za"
#y = re.findall('[0-9]+',x)
## matches everything in the expression but prints only what is in the paranthesis
#y= re.findall('^From: (\S+@\S+)',x)
##print domain
#y = re.findall('@([^ ]*)',x)
#
#stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)')
#
## Non greedy match: Finds the first : and stops matching '^F.+?:'
