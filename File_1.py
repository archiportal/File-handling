# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:54:23 2021

@author: ARCHISMAN ROY
"""

f = open("Ronaldo.txt", "r")
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline())
f.seek(0)
print(f.read(5))
f.seek(0)
for x in f:
  print(x)
f.close()
