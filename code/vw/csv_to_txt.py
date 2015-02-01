# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:02:18 2015

@author: Antoine

python csv_to_txt <csv> <txt> <type>

type can be "train", "validation" or "test"
"""
import sys
from os.path import isfile
from numpy import array
from datetime import datetime

encoding = 'UTF-8'
data_type = sys.argv[3]
skip_header = True
feature_list = array(['hour','C1','banner_pos','site_id','site_domain','site_category','app_id','app_domain','app_category','device_id','device_ip','device_model','device_type','device_conn_type','C14','C15','C16','C17','C18','C19','C20','C21','day'])

try:
    marker = sys.argv[5]
except IndexError:
    marker = ''

if data_type == 'train' or data_type == 'validation':
    col_offset = 2 # Skip the ID and the click
elif data_type == 'test':
    col_offset = 1 # Skip the ID
    
if isfile(sys.argv[2]) :
    sys.exit(1)

In = open(sys.argv[1], 'r') # Open file for to transform (csv)
Out= open(sys.argv[2], 'wb') # Open file to write (txt)

start = datetime.now()

# Start reading the file
for line in In:
    if skip_header == True:
        skip_header = False
        continue
    
    line = line.split(',') # Parse line
    entry = ''
    
    # Keep only the fridays for validation
    if data_type == 'validation':
        value = line[col_offset]
        date = datetime(int('20'+value[0:2]),int(value[2:4]),int(value[4:6]))
        if str(date.strftime('%A')) != 'Friday':
            continue
    
    if data_type == 'train' or data_type == 'validation':
        label = 2 * int(line[1]) - 1
        entry += str(label) + " '" + line[0]
    else:
        entry += "1 '" + line[0]
        
    # First namespace : day and hour
    a = line[col_offset]
    new_date= datetime(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
    day = new_date.strftime("%A")
    hour= a[6:8]
    entry += " |h " + str(hour) + " " + str(day)
    
    # Second namespace : C1, C15, C16, C20
    entry += " |c " + line[col_offset+1] + ' ' + line[col_offset+13] + ' ' + line[col_offset+14] + line[col_offset+18]
    
    # Third namespace : banner position
    entry += " |b " + line[col_offset+2]
    
    # Fourth namespace : site and app
    entry += " |s " + line[col_offset+3]
    
    # Fifth : app
    entry += " |a " + line[col_offset+4]
    
    # Sixth namespace : device
    entry += " |d " + line[col_offset+7] + ' ' + line[col_offset+8] + ' ' + line[col_offset+9] + ' ' + line[col_offset+10] + ' ' + line[col_offset+11]
    
    # Seventh namespace : anonymous features
    entry += " |e " + line[col_offset+12] + ' ' + line[col_offset+15] + ' ' + line[col_offset+16] + ' '+ line[col_offset+17]
    
    # Eighth namespace : C21
    entry += " |l " + line[col_offset+19]
    
    Out.write(bytes(entry + '\n', encoding))
        
print("Task completed in %ss." % (datetime.now() - start))
