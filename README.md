# click


Vowpal Wabbit guide

Install:
sudo apt-get install libboost-all-dev
./configure --with-boost-libdir=/usr/lib/x86_64-linux-gnu​ (needs to be passed the location on Boost)
make
sudo make install (this fails)
make test (also fails)

Test:
./vowpalwabbit/vw -- version

Create data in vw format:
import csv_to_vw
csv_to_vw.csv_to_vw("~/work/click/data/train_random1on100.csv", "~/work/click/data/click.train_original_data.vw",train=True)
csv_to_vw.csv_to_vw("~/work/click/data/test.csv", "~/work/click/data/click.test_original_data.vw",train=False)


Train & test model:
./vw ~/work/click/data/click.train_original_data.vw -f ~/work/click/data/click.model.vw --loss_function logistic
./vw ~/work/click/data/click.test_original_data.vw -t -i ~/work/click/data/click.model.vw -p ~/work/click/data/click.preds.txt
