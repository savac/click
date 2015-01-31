@echo off

set l1=0
set l2=0
set l=1

set settings=-b 18 --loss_function logistic -l %l% --l1 %l1% --l2 %l2% -c --passes 4 --sgd
set interactions=-q ha
rem --cubic abc --cubic abd --cubic abe --cubic abh --cubic abl --cubic abs --cubic acd --cubic ace --cubic ach --cubic acl --cubic acs --cubic ade --cubic adh --cubic adl --cubic ads --cubic aeh --cubic ael --cubic aes --cubic ahl --cubic ahs --cubic als --cubic bcd --cubic bce --cubic bch --cubic bcl --cubic bcs --cubic bde --cubic bdh --cubic bdl --cubic bds --cubic beh --cubic bel --cubic bes --cubic bhl --cubic bhs --cubic bls --cubic cde --cubic cdh --cubic cdl --cubic cds --cubic ceh --cubic cel --cubic ces --cubic chl --cubic chs --cubic cls --cubic deh --cubic del --cubic des --cubic dhl --cubic dhs --cubic dls --cubic ehl --cubic ehs --cubic els --cubic hls

set traincsv=../../data/random1on100.csv
set traintxt=../../data/random1on100.txt
set validationtxt=../../data/validation.txt
set testcsv=../../data/test.csv
set testtxt=../../data/test.txt
set predcsv=../../data/predictions.csv
set predtxt=../../data/predictions.txt
set probacsv=../../data/proba.csv

rem generate files if needed
python csv_to_txt.py %traincsv% %traintxt% train
rem python csv_to_txt.py %testcsv% %testtxt% test

rem train
vw %settings% %interactions% -d %traintxt% -f model.vw

rem validate
vw -t -i model.vw -p %predtxt% -d ../../data/validation.txt
python to_submission.py %predtxt% ../../data/proba.csv
python validate.py ../../data/validation.txt %probacsv%