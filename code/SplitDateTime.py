# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 16:44:55 2015

@author: Antoine

Split the column hour to two columns "hour" and "min" which represent day hours
and minutes. I dropped the day and month because all the data is from the same
day.

Set the csv file to modify below.
"""

file = "../data/train_random1on100.csv";


import numpy as np;
from pandas import read_csv;

#Set data type
types = {
    'id':np.uint64,
    'click':np.bool,
    'hour':np.int32,
};

# Load the data set
data = read_csv(file, header=0, index_col=None, engine='c');  

data['min'] = (data['hour'] % 60).astype(np.int8)
#data['day'] = (data['hour'] / 1000000).astype(int)
#data['month'] = ((data['hour'] - data['day'] * 1000000) / 10000).astype(int)
data['hour'] = ((data['hour'] - data['min']) / 100 % 24).astype(np.int8)

data = data.set_index('id')
data.to_csv("../data/train_hourfixed.csv");