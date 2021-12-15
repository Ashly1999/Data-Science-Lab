#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:02:10 2021

@author: sjcet
"""

import numpy as np
x=np.array([[2,3,4],[5,6,7],[8,9,10]])
print(x)


print(np.power(x,3))
print(np.multiply(x,(x*x)))
print(x*x*x)
print(x**3)

b=np.identity(3,dtype=int)
print(b)

out=np.power(x,x)
print(out)


y = np.arange(11,20).reshape(3,3)

print("perform the operation X^2 +2Y: \n",np.add((np.power(x,2)),(np.multiply(y,2))))