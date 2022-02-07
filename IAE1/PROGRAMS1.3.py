#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:13:51 2022

@author: sjcet
"""

import matplotlib.pyplot as plt 
Maths=(32,68,18,75,38,59,66,92,52,75,48)
English=(74,44,85,19,88,69,50,33,29,32,56)
plt.bar(Maths,edgecolor="blue",height=11)
plt.bar(English,edgecolor="red",height=11)
plt.show()