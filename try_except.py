# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:27:51 2016

@author: Geetha Yedida
"""

largest = None
smallest = None
third = None
while True:
    num = raw_input("Enter a number: ")
    if num=='done':           
            break
    try:
        num = int(num)        
    except ValueError:
        print "Invalid input"
        continue
    if(smallest == None):
        smallest = num
        largest = num
    if(largest <num):
        largest=num
    elif(num<smallest):
        smallest = num      
    third = smallest
print "Maximum is", largest
print "Minimum is", smallest