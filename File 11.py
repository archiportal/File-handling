# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:41:01 2021

@author: ARCHISMAN ROY
"""

with open("Filelow.txt") as f1:
    with open("Fileup.txt" ,"w") as f2:
        for i in f1:
            res=str(i)
            
            f2.write(res.upper())