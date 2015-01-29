@echo off

mkdir ..\..\data
mkdir ..\..\data\SingleFeature
mkdir ..\..\data\SingleFeature\Models
mkdir ..\..\data\SingleFeature\Summary

echo Create training sets...
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/hour.txt train hour
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/day.txt train day
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C1.txt train C1 C1:
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
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C14.txt train C14 C14:
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C15.txt train C15 C15:
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C16.txt train C16 C16:
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C17.txt train C17 C17:
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C18.txt train C18 C18:
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C19.txt train C19 C19:
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C20.txt train C20 C20:
python SingleFeatureSelection.py ../../data/train_random1on100.csv ../../data/SingleFeature/C21.txt train C21 C21:

echo Create validation sets (Fridays only)
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_hour.txt validation hour
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_day.txt validation day
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C1.txt validation C1 C1:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_banner_pos.txt validation banner_pos
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_site_id.txt validation site_id
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_site_domain.txt validation site_domain
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_site_category.txt validation site_category
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_app_id.txt validation app_id
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_device_id.txt validation device_id
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_device_ip.txt validation device_ip
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_device_model.txt validation device_model
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_device_type.txt validation device_type
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_device_conn_type.txt validation device_conn_type
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C14.txt validation C14 C14:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C15.txt validation C15 C15:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C16.txt validation C16 C16:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C17.txt validation C17 C17:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C18.txt validation C18 C18:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C19.txt validation C19 C19:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C20.txt validation C20 C20:
python SingleFeatureSelection.py ../../data/validationAllDays.csv ../../data/SingleFeature/val_C21.txt validation C21 C21:

echo Training
vw -d ../../data/SingleFeature/hour.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/hour.vw --readable_model ../data/SingleFeature/Models/hour.txt > ../../data/SingleFeature/Summary/hour.txt
vw -d ../../data/SingleFeature/day.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/day.vw --readable_model ../data/SingleFeature/Models/day.txt > ../../data/SingleFeature/Summary/day.txt
vw -d ../../data/SingleFeature/C1.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C1.vw --readable_model ../data/SingleFeature/Models/C1.txt > ../../data/SingleFeature/Summary/C1.txt
vw -d ../../data/SingleFeature/banner_pos.txt -b 18 -c --holdout_off --passes 5 --loss_function logistic -f ../data/SingleFeature/Models/banner_pos.vw --readable_model ../data/SingleFeature/Models/banner_pos.txt > ../../data/SingleFeature/Summary/banner_pos.txt
vw -d ../../data/SingleFeature/site_id.txt -b 18 -c --holdout_off --passes 5 --loss_function logistic -f ../data/SingleFeature/Models/site_id.vw --readable_model ../data/SingleFeature/Models/site_id.txt > ../../data/SingleFeature/Summary/site_id.txt
vw -d ../../data/SingleFeature/site_category.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/site_category.vw --readable_model ../data/SingleFeature/Models/site_category.txt > ../../data/SingleFeature/Summary/site_category.txt
vw -d ../../data/SingleFeature/app_id.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/app_id.vw --readable_model ../data/SingleFeature/Models/app_id.txt > ../../data/SingleFeature/Summary/app_id.txt
vw -d ../../data/SingleFeature/device_id.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/device_id.vw --readable_model ../data/SingleFeature/Models/device_id.txt > ../../data/SingleFeature/Summary/device_id.txt
vw -d ../../data/SingleFeature/device_ip.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/device_ip.vw --readable_model ../data/SingleFeature/Models/device_ip.txt > ../../data/SingleFeature/Summary/device_ip.txt
vw -d ../../data/SingleFeature/device_model.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/device_model.vw --readable_model ../data/SingleFeature/Models/device_model.txt > ../../data/SingleFeature/Summary/device_model.txt
vw -d ../../data/SingleFeature/device_type.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/device_type.vw --readable_model ../data/SingleFeature/Models/device_type.txt > ../../data/SingleFeature/Summary/device_type.txt
vw -d ../../data/SingleFeature/device_conn_type.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/device_conn_type.vw --readable_model ../data/SingleFeature/Models/device_conn_type.txt > ../../data/SingleFeature/Summary/device_conn_type.txt
vw -d ../../data/SingleFeature/C14.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C14.vw --readable_model ../data/SingleFeature/Models/C14.txt > ../../data/SingleFeature/Summary/C14.txt
vw -d ../../data/SingleFeature/C15.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C15.vw --readable_model ../data/SingleFeature/Models/C15.txt > ../../data/SingleFeature/Summary/C15.txt
vw -d ../../data/SingleFeature/C16.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C16.vw --readable_model ../data/SingleFeature/Models/C16.txt > ../../data/SingleFeature/Summary/C16.txt
vw -d ../../data/SingleFeature/C17.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C17.vw --readable_model ../data/SingleFeature/Models/C17.txt > ../../data/SingleFeature/Summary/C17.txt
vw -d ../../data/SingleFeature/C18.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C18.vw --readable_model ../data/SingleFeature/Models/C18.txt > ../../data/SingleFeature/Summary/C18.txt
vw -d ../../data/SingleFeature/C19.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C19.vw --readable_model ../data/SingleFeature/Models/C19.txt > ../../data/SingleFeature/Summary/C19.txt
vw -d ../../data/SingleFeature/C20.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C20.vw --readable_model ../data/SingleFeature/Models/C20.txt > ../../data/SingleFeature/Summary/C20.txt
vw -d ../../data/SingleFeature/C21.txt -b 18 -c --passes 5 --holdout_off --loss_function logistic -f ../data/SingleFeature/Models/C21.vw --readable_model ../data/SingleFeature/Models/C21.txt > ../../data/SingleFeature/Summary/C21.txt

echo Validation (on Fridays)
vw -t ../data/SingleFeature/Models/hour.vw > ../../data/SingleFeature/Summary/val_hour.txt
vw -t ../data/SingleFeature/Models/day.vw > ../../data/SingleFeature/Summary/val_day.txt
vw -t ../data/SingleFeature/Models/C1.vw > ../../data/SingleFeature/Summary/val_C1.txt
vw -t ../data/SingleFeature/Models/banner_pos.vw > ../../data/SingleFeature/Summary/val_banner_pos.txt
vw -t ../data/SingleFeature/Models/site_id.vw > ../../data/SingleFeature/Summary/val_site_id.txt
vw -t ../data/SingleFeature/Models/site_category.vw > ../../data/SingleFeature/Summary/val_site_category.txt
vw -t ../data/SingleFeature/Models/app_id.vw > ../../data/SingleFeature/Summary/val_app_id.txt
vw -t ../data/SingleFeature/Models/device_id.vw > ../../data/SingleFeature/Summary/val_device_id.txt
vw -t ../data/SingleFeature/Models/device_ip.vw > ../../data/SingleFeature/Summary/val_device_ip.txt
vw -t ../data/SingleFeature/Models/device_model.vw > ../../data/SingleFeature/Summary/val_device_model.txt
vw -t ../data/SingleFeature/Models/device_type.vw > ../../data/SingleFeature/Summary/val_device_type.txt
vw -t ../data/SingleFeature/Models/device_conn_type.vw > ../../data/SingleFeature/Summary/val_device_conn_type.txt
vw -t ../data/SingleFeature/Models/C14.vw > ../../data/SingleFeature/Summary/val_C14.txt
vw -t ../data/SingleFeature/Models/C15.vw > ../../data/SingleFeature/Summary/val_C15.txt
vw -t ../data/SingleFeature/Models/C16.vw > ../../data/SingleFeature/Summary/val_C16.txt
vw -t ../data/SingleFeature/Models/C17.vw > ../../data/SingleFeature/Summary/val_C17.txt
vw -t ../data/SingleFeature/Models/C18.vw > ../../data/SingleFeature/Summary/val_C18.txt
vw -t ../data/SingleFeature/Models/C19.vw > ../../data/SingleFeature/Summary/val_C19.txt
vw -t ../data/SingleFeature/Models/C20.vw > ../../data/SingleFeature/Summary/val_C20.txt
vw -t ../data/SingleFeature/Models/C21.vw > ../../data/SingleFeature/Summary/val_C21.txt