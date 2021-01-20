# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:36:44 2021

@author: ARCHISMAN ROY
"""

f1=open("File4.txt","w+")
s1='Hola\n'
s2='I am Archisman Roy.\n'
lst=[s1,s2]
f1.writelines(lst)

f1.close()

with open('File4.txt') as readf, open('File5.txt','w') as writef:
    for line in reversed(readf.readlines()):
        writef.write(line)