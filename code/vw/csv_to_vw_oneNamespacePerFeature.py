-*- coding: utf-8 -*-
"""
Created on Tue Feb  3 23:52:23 2015

@author: erostate

type can be "train", "validation" 
can skip records on keep only some records if needed
will skip/keep last day on train/validation
command line format is: 
$pypy csv_to_vwoneNamespacePerFeature.py filetoread filetowrite train 
$pypy csv_to_vwoneNamespacePerFeature.py filetoread filetowrite validation
"""

import sys
from datetime import datetime

encoding = 'UTF-8'
data_type = sys.argv[3]

feature_list = ['C1','banner_pos','site_id','site_domain','site_category','app_id','app_domain','app_category','device_id','device_ip','device_model','device_type','device_conn_type','C14','C15','C16','C17','C18','C19','C20','C21']

#records to skip/keep
linesToSkip={}
keepOnlyLines={}
if data_type=='train':
    linesToSkip['date'] = '20141030'
elif data_type=='validation':
    keepOnlyLines['date'] = '20141030'
    
#get file path from command line arguments
fileinpath = sys.argv[1]
fileoutpath=sys.argv[2]

print('Converting file %s to VW format, output to file %s'%(fileinpath,fileoutpath))
for feature,value in linesToSkip.items():
    print('Skipping lines where %s=%s'%(feature,value))
for feature,value in keepOnlyLines.items():
    print('Keeping only lines where %s=%s'%(feature,value))

filein = open(fileinpath, 'r') # Open file for to transform (csv)
fileout = open(fileoutpath, 'wb') # Open file to write (txt)

start = datetime.now()

#get headers, remove end of line
headers = filein.readline()
headers = headers[:-2].split(',')

#define namespaces
#namespaces contains as key the namespace letters, and as values the feature names
namespaces = {}
namespaces['h'] = ['hour']
namespaces['w'] = ['weekday']
#namespaces['c'] = ['C1','C14','C15','C16','C17','C18','C19','C20','C21']
#namespaces['b'] = ['banner_pos']
#namespaces['s'] = ['site_id','site_domain','site_category']
#namespaces['a'] = ['app_id','app_domain','app_category']
#namespaces['d'] = ['device_id','device_ip','device_model','device_type','device_conn_type']

#get some letters for namespaces
namespacesKeys = map(chr,range(ord('a'),ord('z')+1))
namespacesKeys.remove('h') #already used this letter
namespacesKeys.remove('w') #already used this letter

for i in xrange(len(feature_list)):
    namespaces[namespacesKeys[i]] = [feature_list[i]]

print('Namespace \t Feature')
for namespace,feature in namespaces.items():
    print('%s \t %s'%(namespace,feature))
    
countRecords = 0
keptRecords = 0
skippedRecords = 0

# Start reading the file
for line in filein:
    
    countRecords += 1    
    
    #read line
    line = line[:-2].split(',') # Parse line
    lined = dict(zip(headers, line))

    #format date
    daten = lined['hour']
    hour = daten[6:8]
    year = int('20'+daten[0:2])
    month = int(daten[2:4])
    day = int(daten[4:6])
    #date = datetime(year,month,day)
    #weekday = str(date.strftime('%A'))
    weekday = day%7 #faster

    lined['hour'] = hour
    lined['weekday'] = weekday
    lined['date'] = '%s%s%s'%(year,month,day) 
    
    if lined.has_key('click'):
        label = 2 * int(lined['click']) - 1
    else:
        label = 1
        
    #check if we should skip this line
    skip = False
    for feature, value in linesToSkip.items():
        if lined[feature]==value:
            skip = True
            break
    if not(skip):
        for feature,value in keepOnlyLines.items():
            if lined[feature]!=value:
                skip = True
                break
    if skip: 
        skippedRecords += 1
        continue

    keptRecords += 1

    #creating entry
    entry = str(label) + ' |'
    
    #adding features
    values = [' '.join(str(lined[feature]) for feature in features) for features in namespaces.values()]
    nameFeat = zip(namespaces.keys(),values) 
    entry += '|'.join('%s %s' % t for t in nameFeat)
    
    #print entry 
    fileout.write(entry + '\n')        
    
print("Task completed in %ss, processed %d lines, kept %d lines, skipped %d lines"% (datetime.now() - start, countRecords, keptRecords, skippedRecords ))
