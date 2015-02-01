# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:22:46 2015

@author: Antoine

python Validate.py <reference_file> <predictions_file>

"""

import sys
from math import log

class_file = open(sys.argv[1], 'r') # The txt file from the csv
pred_file = open(sys.argv[2], 'r') # The csv from the predictions

def logloss(p, y):
    ''' FUNCTION: Bounded logloss

        INPUT:
            p: our prediction
            y: real answer

        OUTPUT:
            logarithmic loss of p given y
    '''
    p = max(min(p, 1. - 10e-15), 10e-15) # tolerance
    return log(p) if y == 1 else log(1. - p)
    
s = 0 # sum of errors
l = 0 # Sum of logloss
n = 0 # count of examples
pred_file.readline()
for line1 in class_file:
    line2 = pred_file.readline()
    
    column1 = line1.split(' ')
    column2 = line2.split(',')
    
    p1 = float(column1[0])
    p2 = float(column2[1])
    
    if ((p1 > 0.5) != (p2 > 0.5)):
        s += 1
    l += logloss(p2,p1)
    n += 1
print('error=' + str(s / n))
print('logloss=' + str(-l / n))



    