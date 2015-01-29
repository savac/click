# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:02:18 2015

@author: Antoine

Create a new data set with only one feature at the vw format
"""
import sys
from os.path import isfile
from numpy import array,where
from datetime import datetime

encoding = 'UTF-8'
data_type = sys.argv[3]
skip_header = True
feature_list = array(['hour','C1','banner_pos','site_id','site_domain','site_category','app_id','app_domain','app_category','device_id','device_ip','device_model','device_type','device_conn_type','C14','C15','C16','C17','C18','C19','C20','C21','day'])
selected_feature = where(feature_list == sys.argv[4])[0][0]
try:
    marker = sys.argv[5]
except IndexError:
    marker = ''

if feature_list[selected_feature] == 'app_domain' or feature_list[selected_feature] == 'app_category':
    print("app_domain and app_category should not be used.")
    exit

if data_type == 'train' or data_type == 'validation':
    col_offset = 2 # Skip the ID and the click
elif data_type == 'test':
    col_offset = 1 # Skip the ID
    
if isfile(sys.argv[2]) :
    print('File "' + sys.argv[2] + '" already exist.')
    exit

In = open(sys.argv[1], 'r') # Open file for to transform (csv)
Out= open(sys.argv[2], 'wb') # Open file to write (txt)

start = datetime.now()

# Start reading the file
for line in In:
    if skip_header == True:
        skip_header = False
        continue
    
    line = line.split(',') # Parse line
    
    # Keep only the fridays for validation
    if data_type == 'validation':
        value = line[col_offset]
        date = datetime(int('20'+value[0:2]),int(value[2:4]),int(value[4:6]))
        if str(date.strftime('%A')) != 'Friday':
            continue
    
    if feature_list[selected_feature] == 'hour':
        value = line[col_offset+selected_feature][6:8]
    elif feature_list[selected_feature] == 'day':
        value = line[col_offset]
        date = datetime(int('20'+value[0:2]),int(value[2:4]),int(value[4:6]))
        value = str(date.strftime('%A'))
    else:
        value = line[col_offset+selected_feature]

    label = 2 * int(line[1]) - 1
    if data_type == 'train' or data_type == 'validation':
        Out.write(bytes(label + " '" + line[0] + ' | ' + marker + value + '\n', encoding))
    elif data_type == 'test':
        Out.write(bytes("1 '" + line[0] + ' | ' + marker + value + '\n', encoding))
        
print("Task finished in %s." % (datetime.now() - start))