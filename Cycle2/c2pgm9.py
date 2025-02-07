#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:01:31 2021

@author: sjcet
"""

import numpy as np

array_1d=np.arange(1,6).reshape((1,5))
print("1D array\n",array_1d)
print("use of diag() function in 1D array.")
x=np.diag(array_1d)
print(x,"\n")

array_2d=np.arange(9).reshape((3,3))
print("2D array\n",array_2d)
print("use of diag() function in 2D array.")
y=np.diag(array_2d)
print(y)