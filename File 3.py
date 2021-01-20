# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:54:46 2021

@author: ARCHISMAN ROY
"""

f = open("Ronaldo.txt", "w")
f.write("Oops! The file is deleted.")
f.close()
#open and read the file after the appending:
f = open("Ronaldo.txt", "r")
print(f.read())
