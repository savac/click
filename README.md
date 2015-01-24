# click


Vowpal Wabbit guide

Install:<br />
sudo apt-get install libboost-all-dev<br />
./configure --with-boost-libdir=/usr/lib/x86_64-linux-gnu​ (needs to be passed the location on Boost)<br />
make<br />
sudo make install (this fails)<br />
make test (also fails)<br />

Test:<br />
./vowpalwabbit/vw -- version<br />

Create data in vw format:<br />
import csv_to_vw<br />
csv_to_vw.csv_to_vw("~/work/click/data/train_random1on100.csv", "~/work/click/data/click.train_original_data.vw",train=True)<br />
csv_to_vw.csv_to_vw("~/work/click/data/test.csv", "~/work/click/data/click.test_original_data.vw",train=False)<br />


Train & test model:<br />
./vw ~/work/click/data/click.train_original_data.vw -f ~/work/click/data/click.model.vw --loss_function logistic<br />
./vw ~/work/click/data/click.test_original_data.vw -t -i ~/work/click/data/click.model.vw -p ~/work/click/data/click.preds.txt<br />
