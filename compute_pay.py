# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
hrs = raw_input("Enter Hours:")
h = float(hrs)
if int(h) <= 40:
    pay = h * 10.5
    print pay
else:
    newhr = h - 40
    pay = float(newhr) * 1.5 * 10.5
    pay = pay + 10.5*40
    print pay
