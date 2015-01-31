@echo off

mkdir ..\..\data 2>NUL
mkdir ..\..\data\SingleFeature 2>NUL
mkdir ..\..\data\SingleFeature\Models 2>NUL
mkdir ..\..\data\SingleFeature\train 2>NUL
mkdir ..\..\data\SingleFeature\validation 2>NUL

echo Create training sets...
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/hour.txt train hour
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/day.txt train day
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C1.txt train C1
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/banner_pos.txt train banner_pos
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/site_id.txt train site_id
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/site_domain.txt train site_domain
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/site_category.txt train site_category
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/app_id.txt train app_id
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/device_id.txt train device_id
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/device_ip.txt train device_ip
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/device_model.txt train device_model
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/device_type.txt train device_type
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/device_conn_type.txt train device_conn_type
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C14.txt train C14
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C15.txt train C15
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C16.txt train C16
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C17.txt train C17
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C18.txt train C18
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C19.txt train C19
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C20.txt train C20
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C21.txt train C21

echo Create validation sets (Fridays only)
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/hour.txt validation hour
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/day.txt validation day
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C1.txt validation C1
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/banner_pos.txt validation banner_pos
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/site_id.txt validation site_id
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/site_domain.txt validation site_domain
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/site_category.txt validation site_category
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/app_id.txt validation app_id
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/device_id.txt validation device_id
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/device_ip.txt validation device_ip
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/device_model.txt validation device_model
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/device_type.txt validation device_type
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/device_conn_type.txt validation device_conn_type
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C14.txt validation C14
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C15.txt validation C15
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C16.txt validation C16
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C17.txt validation C17
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C18.txt validation C18
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C19.txt validation C19
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C20.txt validation C20
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/validation/C21.txt validation C21

echo Training
set settings=-b 18 -c --passes 10 --l1 0 --l2 0 --sgd --holdout_off --loss_function logistic
vw %settings% -d ../../data/SingleFeature/hour.txt -f ../../data/SingleFeature/Models/hour.vw
vw %settings% -d ../../data/SingleFeature/day.txt -f ../../data/SingleFeature/Models/day.vw
vw %settings% -d ../../data/SingleFeature/C1.txt -f ../../data/SingleFeature/Models/C1.vw
vw %settings% -d ../../data/SingleFeature/banner_pos.txt -f ../data/SingleFeature/Models/banner_pos.vw
vw %settings% -d ../../data/SingleFeature/site_id.txt -f ../../data/SingleFeature/Models/site_id.vw
vw %settings% -d ../../data/SingleFeature/site_category.txt -f ../data/SingleFeature/Models/site_category.vw
vw %settings% -d ../../data/SingleFeature/app_id.txt -f ../../data/SingleFeature/Models/app_id.vw
vw %settings% -d ../../data/SingleFeature/device_id.txt -f ../data/SingleFeature/Models/device_id.vw
vw %settings% -d ../../data/SingleFeature/device_ip.txt -f ../data/SingleFeature/Models/device_ip.vw
vw %settings% -d ../../data/SingleFeature/device_model.txt -f ../data/SingleFeature/Models/device_model.vw
vw %settings% -d ../../data/SingleFeature/device_type.txt -f ../data/SingleFeature/Models/device_type.vw
vw %settings% -d ../../data/SingleFeature/device_conn_type.txt -f ../data/SingleFeature/Models/device_conn_type.vw
vw %settings% -d ../../data/SingleFeature/C14.txt -f ../../data/SingleFeature/Models/C14.vw
vw %settings% -d ../../data/SingleFeature/C15.txt -f ../../data/SingleFeature/Models/C15.vw
vw %settings% -d ../../data/SingleFeature/C16.txt -f ../../data/SingleFeature/Models/C16.vw
vw %settings% -d ../../data/SingleFeature/C17.txt -f ../../data/SingleFeature/Models/C17.vw
vw %settings% -d ../../data/SingleFeature/C18.txt -f ../../data/SingleFeature/Models/C18.vw
vw %settings% -d ../../data/SingleFeature/C19.txt -f ../../data/SingleFeature/Models/C19.vw
vw %settings% -d ../../data/SingleFeature/C20.txt -f ../../data/SingleFeature/Models/C20.vw
vw %settings% -d ../../data/SingleFeature/C21.txt -f ../../data/SingleFeature/Models/C21.vw

echo Validation (on Fridays)
vw -t -i ../../data/SingleFeature/Models/hour.vw
vw -t -i ../../data/SingleFeature/Models/day.vw
vw -t -i ../../data/SingleFeature/Models/C1.vw
vw -t -i ../../data/SingleFeature/Models/banner_pos.vw
vw -t -i ../../data/SingleFeature/Models/site_id.vw
vw -t -i ../../data/SingleFeature/Models/site_category.vw
vw -t -i ../../data/SingleFeature/Models/app_id.vw
vw -t -i ../../data/SingleFeature/Models/device_id.vw
vw -t -i ../../data/SingleFeature/Models/device_ip.vw
vw -t -i ../../data/SingleFeature/Models/device_model.vw
vw -t -i ../../data/SingleFeature/Models/device_type.vw
vw -t -i ../../data/SingleFeature/Models/device_conn_type.vw
vw -t -i ../../data/SingleFeature/Models/C14.vw
vw -t -i ../../data/SingleFeature/Models/C15.vw
vw -t -i ../../data/SingleFeature/Models/C16.vw
vw -t -i ../../data/SingleFeature/Models/C17.vw
vw -t -i ../../data/SingleFeature/Models/C18.vw
vw -t -i ../../data/SingleFeature/Models/C19.vw
vw -t -i ../../data/SingleFeature/Models/C20.vw
vw -t -i ../../data/SingleFeature/Models/C21.vw