# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:44:01 2016

@author: Geetha Yedida
"""


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)
words = list()
for line in text:
    if line.startswith("From "):
        sub = line.split()
        words.append(sub[1])
        
counts = dict()
for word in words:
    counts[word] = counts.get(word,0)+1
    
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count >bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount


#ddd = dict()
#ddd['age'] = 21
#ddd['course'] = 192
#ddd['age'] = 32
#print 'age' in ddd
#
#jjj = {'chuck':1,'fred' : 23, 'jan':100}
#for key in jjj:
#    print key, jjj[key]
#for aaa,bbb in jjj.items():
#    print aaa,bbb
#    
#ooo = {}
#print list(ooo)
#print ooo.keys()
#print ooo.values()
#print ooo.items()
#
#
#c = dict()
#names = ['geetha','harshini','yedida']
#for name in names:
#    c[name] =  c.get(name,0) +1
#print c