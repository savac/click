#!/bin/bash 

vwloc="/home/sc/work/vowpal_wabbit-7.9/vowpalwabbit/vw"


echo "================================================================"
echo "Data munging:"

# Convert to vw format, shuffle and then split for training and validation
#python -c "import vw_utils;vw_utils.csv_to_vw('train.csv', 'train.vw',train=True)"
#shuf-t train.vw -o train_shuffled.vw
#python -c "import vw_utils;vw_utils.splitfast('train_shuffled.vw', 'train_part_', 0.90)" # **** NB: shuffled ****

echo "================================================================"
echo "Training:"

# OPTIONS
# -b: number of bits for the hash function (default: 18) nb: large sets prefer 22, 8GB allow b=28
# -c --passes 10 --holdout_off: if we want to overfit like mad, nb: small improvement from more passes
# -l: learning rate, a too high learning rate may over-fit (default: 0.5)
# --power_t: power on the learning rate decay (default: 0.5)
# --noconstant: VW has a default constant feature, this removes it.

# REGULARISATION
# --l1: lasso regularization (basically this is feature selection)
# --l2: ridge regularization
# nb: does not work well for large sets. l1 = 1e-7 ideal for small set, but large sets prefer no regularisation

# FEATURES
# -q ab: quadratic features between all features in namespace a* and b*, 
#         -q cc: massive improvement >0.01 but slow as to many features
#         -q hc: good improvement ~0.01 and fast as only ~x2 features

# TRAINING
# --bfgs: use batch lbfgs instead of stochastic gradient descent. nb: very poor
# --nn: neural network nb: not yet

# SVM
# --ksvm: enable
# --reprocess: Number of reprocess steps through (default 1)
# --kernel: Kernel type through . Supported types: linear, poly, rbf
# --kernel linear
# --kernel poly. Additionally takes --degree d (default 2)
# --kernel rbf. Additionally takes --bandwidth b (default 1.0)
# --l2: Do not forget to specify regularization through
# nb: deadslow
#  --ksvm\
#  --reprocess 2\
#  --kernel linear\
#  --l2 1e-7\
#  -q hd -q hs -q ha -q hn -q ds -q da -q dn -q se -q sn -q ae\
#  -q hd -q hs -q ha -q hn -q ds -q da -q dn -q se -q sn -q ae\

$vwloc\
 train_part_00\
  -b 28\
  -c --passes 3\
  --early_terminate 2\
  -l 0.4\
  --power_t 0.4\
  --l1 1e-8\
  --l2 0\
  -q hd -q hs -q ha -q hn -q ds -q da -q dn -q se -q sn -q ae\
  -f click.model.vw\
  --loss_function logistic

#default:
#$vwloc\
# train_part_00\
#  -b 18\
#  -c --passes 1\
#  -l 0.5\
#  --power_t 0.5\
#  -f click.model.vw\
#  --loss_function logistic

echo "================================================================"
echo "Testing:"
    
$vwloc\
 train_part_01\
  -t -i click.model.vw\
   -p train_part_01_preds.txt
   
python -c "import vw_utils;vw_utils.create_submission('train_part_01_preds.txt', 'train_part_01_submission.txt')"
python -c "import vw_utils;vw_utils.logloss_total('train_part_01_submission.txt', 'train_part_01')"

# Create submission for the actual test set
#python -c "import vw_utils;vw_utils.csv_to_vw('test.csv', 'test.vw',train=False)"
#$vwloc test.vw -t -i click.model.vw -p test_preds.txt
#python -c "import vw_utils;vw_utils.create_submission('test_preds.txt', 'test_submission.txt')"

