#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:42:45 2021

@author: sjcet
"""

import numpy as np
x = np.array([[2, 4, 6], [6.5, 8, 10]])
print(type(x))
print(x)
numOfRows = np. size(x, 0)
print(numOfRows)
numOfColumns = np. size(x, 1)
print(numOfColumns)
print("No. of dimensions: ", x.ndim)
rs=np.reshape(x, (3, 2))
print(rs)