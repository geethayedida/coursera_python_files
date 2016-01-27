# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:58:19 2016

@author: Geetha Yedida
"""
#get input
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)
words = list()
words2 = list()
#if line starts with from, grab the 6th element and slice the time out of it
for line in text:
    if line.startswith("From "):
        sub = line.split()
        words.append(sub[5])

for word in words:
    temp1,temp2,temp3 = word.split(':')
    words2.append(temp1)

# Now, the words2 has the hour part
#count the hours, resulting is a dictionary with hours and count
counts = dict()
for word in words2:
    counts[word] = counts.get(word,0)+1
    
lst = list()
for key,val in counts.items():
    lst.append((key,val))
lst.sort()
for key,val in lst[:10]:
    print key,val