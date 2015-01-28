# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 09:51:12 2015

@author: Antoine
"""

import sys
from datetime import datetime

In = open(sys.argv[1], 'r') # Open file for to transform
Out= open(sys.argv[2], 'wb') # Open file to write
line_count=0
start = datetime.now()
counter=0

for line in In:
    if line_count==0:
        line_count=1
        continue    
    
    categorical_features = ""
    counter+=1
    line = line.split(",")
    
    a = line[2]
    new_date= datetime(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
    day = new_date.strftime("%A")
    hour= a[6:8]
    if day != "Friday":
        continue
    categorical_features += "|hr %s" % hour
    categorical_features += " |day %s" % day

    # 24 columns in data    
    
    # banner position
    categorical_features += " |b"
    categorical_features += " %s" % (line[4-1]) 
    
    # site
    categorical_features += " |site"
    for i in range(5,8):
        categorical_features += " %s" % (line[i-1])
            
    # app
    categorical_features += " |app"
    for i in range(8,11):
        categorical_features += " %s" % (line[i-1])
            
    # device
    categorical_features += " |e"
    for i in range(11,16):
        categorical_features += " %s" % (line[i-1])
    
    # C1, C14-21
    categorical_features += " |num"
    for i in [3] + list(range(16,24)):
        categorical_features += " n%s:%s" % (str(i),line[i-1].strip('\n'))
    # Write to the file    
    Out.write(bytes("1 '%s %s\n" % (line[0],categorical_features), 'UTF-8'))
print("Task execution time:\t%s"%str(datetime.now() - start))