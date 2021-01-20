# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:40:16 2021

@author: ARCHISMAN ROY
"""

with open("File2.txt") as f1:
    with open("File3.txt" ,"w") as f2:
        for i in f1:
            f2.write(i)