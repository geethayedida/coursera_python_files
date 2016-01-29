# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:33:21 2016

@author: Geetha Yedida
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

#import urllib
#fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#for line in fhand:
#    print line.strip()