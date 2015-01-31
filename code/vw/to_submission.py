# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 23:16:05 2015

@author: Antoine

python to_submission.py <predictions> <csv_file_to_create>
"""

import sys
from math import exp

def to_prob(x):
    return 1.0 / (1.0+exp(-x))

prediction_file = open(sys.argv[1],'r')
probabilities_file = open(sys.argv[2],'w')

probabilities_file.write("id,click\n")

for line in prediction_file:
    field = line.split(' ')
    probabilities_file.write(field[1][1:-1] + ',' + str(to_prob(float(field[0]))) + '\n')