# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:56:28 2021

@author: ARCHISMAN ROY
"""

import os
if os.path.exists("Ronaldo.txt"):
    os.remove("Ronaldo.txt")
else:
    print("The file does not exist.")

