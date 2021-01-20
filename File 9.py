# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:27:18 2021

@author: ARCHISMAN ROY
"""

import filecmp
f1=open("File2.txt","w+")
s1='Hola\n'
s2='I am Archisman Roy.\n'
lst=[s1,s2]
f1.writelines(lst)

f1.close()

f1=open("File3.txt","w+")
s1='Hola\n'
s2='I am Archisman Roy.\n'
lst=[s1,s2]
f1.writelines(lst)

f1.close()

F1='File2.txt'
F2='File3.txt'

comp=filecmp.cmp(F1,F2)
print(comp)