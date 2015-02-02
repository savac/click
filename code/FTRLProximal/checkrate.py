# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 19:11:48 2015

@author: erostate

"""
from csv import DictReader

def checkRate(filepath):
#    outputs the click probability in file
    count = 0;
    proba = 0;
    for t, row in enumerate(DictReader(open(filepath))):
        # process id
        count+=1
        proba+=float(row['click'])
    proba /= count;
    print 'found average click proba of %2.4f for %.0f entries in file %s \n'%(proba,count,filepath)
    
#myfile = 'data/submissiontest.csv'
#myfile = 'data/sub4.csv'
#checkRate(myfile)

def shift(filepath,newfilepath,shiftratio):
    #    multiply all probabilities in filepathby shiftratio
    #   and write to newfilepath
    print 'shifting click proba from file %s by %2.4f and writing to %s \n'%(filepath,shiftratio,newfilepath)
    with open(newfilepath, 'w') as outfile:
        outfile.write('id,click\n')
        count = 0;
        totalproba = 0;
        for t, row in enumerate(DictReader(open(filepath))):
            # process id
            myid=row['id']
            
            proba=float(row['click'])
            proba*=shiftratio
            
            totalproba+=proba
            count +=1;
            
            outfile.write('%s,%s\n' % (myid, str(proba)))
            
    totalproba /= count;
    print 'new average click proba of %2.4f for %.0f entries in new file %s \n'%(totalproba,count,newfilepath)
    
mynewfile = 'data/sub4shift.csv'
myfile = 'data/sub4.csv' 
shift(myfile, mynewfile,0.1612/0.1747)
    