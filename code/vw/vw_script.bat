@echo off
echo "Converting to the vw format"
rem python -c "import vw_utils;vw_utils.csv_to_vw('../../data/train_random1on100.csv', '../../data/train.txt',train=True)"
rem python -c "import vw_utils;vw_utils.csv_to_vw('../../data/validation.csv', '../../data/validation.txt',train=False)"


echo vw version & vw --version
echo.

echo "Training"
rem -f Predictor.vw -t ../../data/validation.txt
vw -d ../../data/train.txt -b 18 -p ../../data/predictions.txt --loss_function logistic