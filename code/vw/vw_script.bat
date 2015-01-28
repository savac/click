@echo off
echo "Converting to the vw format"
python -c "import vw_utils;vw_utils.csv_to_vw('../../data/train_random1on100.csv', '../../data/train.vw',train=True)"
python -c "import vw_utils;vw_utils.csv_to_vw('../../data/validation.csv', '../../data/validation.vw',train=False)"

echo "Training"
rem vw ../../data/train.vw -b 28 -c --passes 3 --early_terminate 2 -l 0.4 --
