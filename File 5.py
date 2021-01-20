# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:02:12 2021

@author: ARCHISMAN ROY
"""

with open("File1.txt") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        print(word) 
file.close()
