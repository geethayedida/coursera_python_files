# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:11:02 2016

@author: Geetha Yedida
"""

x = ('Glenn','Sally', 'Joseph')
print x[2]

# immutable y[2] = 0 results in error
#cannot sort, reverse, append
# can count, index
y = (1,9,2)
print max(y)
for iter in y:
    print iter

k,v = (2,45)

d = dict()
d['a'] = 2
d['b']=4
d['c'] = 10

#sort items in dictionary and store them in tuple
tups= sorted(d.items())

#sort by values
temp = list()
for k,v in d.items():
    temp.append((v,k))
temp.sort(reverse=True)

#comparable
(0,1,2)<(4,3,2)
('sam','jane')>('anita','shepord')

# top 10 most common words - list comprehension
print sorted([(v,k) for k,v in d.items()])

