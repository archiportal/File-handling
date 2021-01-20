# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:21:34 2021

@author: ARCHISMAN ROY
"""

words=0
with open("Ronaldo.txt","r") as f:
       for line in f:
           w=line.split()
           words=words + len(words)
max_len=len(max(w,key=len))
print(words)
