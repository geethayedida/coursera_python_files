# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:02:39 2016

@author: Geetha Yedida
"""

def computepay(h,r):
    if(h>40):
        newhr = h - 40
        pay = r * 1.5 * float(newhr)
        pay = float(pay) + 40 * float(rate)
        return float(pay)
    else:
        pay = h * r
        return float(pay)

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate")
p = computepay(float(hrs),float(rate))
print p