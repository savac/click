import math
from datetime import datetime
import subprocess
from itertools import izip

def csv_to_vw(loc_csv, loc_output, train=True):
    start = datetime.now()
    print("\nTurning %s into %s. Is_train_set? %s"%(loc_csv,loc_output,train))
    i = open(loc_csv, "r")
    j = open(loc_output, 'wb')
    counter=0
    with i as infile:
        line_count=0
        for line in infile:
            # to counter the header
            if line_count==0:
                line_count=1
                continue
            # The data has all categorical features
            #numerical_features = ""
            categorical_features = ""
            counter = counter+1
            #print counter
            line = line.split(",")
            if train:
                #working on the date column. We will take day , hour
                a = line[2]
                new_date= datetime(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
                day = new_date.strftime("%A")
                hour= a[6:8]
                categorical_features += " |hr %s" % hour
                categorical_features += " |day %s" % day
                # 24 columns in data    
                for i in range(3,24):
                    if line[i] != "":
                        categorical_features += "|c%s %s" % (str(i),line[i])
            else:
                a = line[1]
                new_date= datetime(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
                day = new_date.strftime("%A")
                hour= a[6:8]
                categorical_features += " |hr %s" % hour
                categorical_features += " |day %s" % day
                for i in range(2,23):
                    if line[i] != "":
                        categorical_features += " |c%s %s" % (str(i+1),line[i])
  #Creating the labels
            #print "a"
            if train: #we care about labels
                if line[1] == "1":
                    label = 1
                else:
                    label = -1 #we set negative label to -1
                #print (numerical_features)
                #print categorical_features
                j.write( "%s '%s %s\n" % (label,line[0],categorical_features))

            else: #we dont care about labels
                #print ( "1 '%s |i%s |c%s\n" % (line[0],numerical_features,categorical_features) )
                j.write( "1 '%s %s\n" % (line[0],categorical_features) )

  #Reporting progress
            #print counter
            if counter % 1000000 == 0:
                print("%s\t%s"%(counter, str(datetime.now() - start)))

    print("\n %s Task execution time:\n\t%s"%(counter, str(datetime.now() - start)))

#csv_to_vw("/Users/RahulAgarwal/kaggle_cpr/train", "/Users/RahulAgarwal/kaggle_cpr/click.train_original_data.vw",train=True)
#csv_to_vw("/Users/RahulAgarwal/kaggle_cpr/test", "/Users/RahulAgarwal/kaggle_cpr/click.test_original_data.vw",train=False)


def zygmoid(x):
    return 1 / (1 + math.exp(-x))

def create_submission(f_in, f_out):
    with open(f_out,"wb") as outfile:
        outfile.write("id,click\n")
        for line in open(f_in):
            
            row = line.strip().split(" ")
            try:
                outfile.write("%s,%f\n"%(row[1],zygmoid(float(row[0]))))
            except:
                pass

def logloss(p, y):
    ''' FUNCTION: Bounded logloss

        INPUT:
            p: our prediction
            y: real answer

        OUTPUT:
            logarithmic loss of p given y
    '''
    p = max(min(p, 1. - 10e-15), 10e-15)
    return -math.log(p) if y == 1. else -math.log(1. - p)
    
    
def logloss_total(f_preds, f_original):
    loss = 0.
    counter = 0
    f1 = open(f_preds, "r")
    f1.readline() # skip the header line
    f2 = open(f_original, 'r')
    while True:
        f2_line = f2.readline()
        if f2_line == "\n":
            continue
        if f2_line == "":
            break
        f1_line = f1.readline() 
        
        f1_line = f1_line.split(",")
        f2_line = f2_line.split(" ")
                
        p = float(f1_line[1])
        if int(f2_line[0])>0:
            y = 1 
        else:
            y = 0
        
        counter += 1
        loss += logloss(p, y)
    return loss/counter


def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])


def splitfast(f_in, f_out_prefix, frac=0.8):
    ''' Split training set file <f_in> in two files called <f_out_prefix> followed by '00/01. 
        <frac> determines the fraction. 
    '''
    t = file_len(f_in)
    m = int(round(t * frac))
    p = subprocess.Popen(['split', '-l', str(m), '-d', f_in, f_out_prefix], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)

