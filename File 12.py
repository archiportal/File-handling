# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:44:14 2021

@author: ARCHISMAN ROY
"""

fnames = ['File6.txt', 'File7.txt'] 

with open('File8.txt' ,'w') as comp:

    for i in fnames:
        with open(i) as f:
            comp.write(f.read())

        comp.write('\n')