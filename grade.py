# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:49:00 2016

@author: Geetha Yedida
"""

i = raw_input("Enter score")
score = float(i)
if score < 0.0 or score > 1.0:
    print ("Bad Score entered")
elif(score >= 0.9 ):
    print 'A'
elif(score >=0.8):
    print 'B'
elif(score >= 0.7):
    print 'C'
elif(score >=0.6):
    print 'D'
else:
    print 'F'