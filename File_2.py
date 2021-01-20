# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:52:45 2021

@author: ARCHISMAN ROY
"""

f = open("Ronaldo.txt", "a")
f.write("He is my idol.")
f.close()
#open and read the file after the appending:
f = open("Ronaldo.txt", "r")
print(f.read())
