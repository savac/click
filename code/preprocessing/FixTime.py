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


from pandas import read_csv;

# Load the data set
data = read_csv(file, header=0, index_col=None, engine='c');  

minutes = (data['hour'] % 60).astype(np.int8)
data['hour'] = (((((data['hour'] % 10000) - minutes) / 100) % 24) * 60 + minutes).astype(np.uint);

data = data.set_index('id')
data.to_csv("../data/train_hourfixed.csv");