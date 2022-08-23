# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 20:06:07 2022

@author: jleroy1


First Assignment: find the sum of dirst 100 integers.
15 August 2022
"""

import numpy as np

list100 =np.linspace(1, 100, 100, dtype=int)
sum100 = sum(list100)

print('sum of the first 100 numbers is: {}' .format(sum100))
#print('sum of the first 100 numbers is: {}' .format(list100))




otherSum = 0
for i in range(101):
    otherSum += i

print('otherSum = {}'.format(otherSum))