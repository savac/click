#### Vowpal Wabbit guide

##### Install
sudo apt-get install libboost-all-dev<br />
./configure --with-boost-libdir=/usr/lib/x86_64-linux-gnu​ (needs to be passed the location on Boost)<br />
make<br />
sudo make install (this fails)<br />
make test (also fails)<br />
vw -- version<br />

##### Create data in vw format
import vw_utils<br />
vw_utils.csv_to_vw("train_random1on100.csv", "click.train_original_data.vw",train=True)<br />
vw_utils.csv_to_vw("test.csv", "click.test_original_data.vw",train=False)<br />

##### Train & test model
vw_utils.splitfast('click.train_original_data.vw', 'train_part_', 0.8)<br />

vw train_part_00 -f click.model.vw --loss_function logistic<br />
vw train_part_01 -t -i click.model.vw -p train_part_01_preds.txt<br />

vw_utils.create_submission('train_part_01_preds.txt', 'train_part_01_submission.txt')<br />
vw_utils.logloss_total('train_part_01_submission.txt', 'train_part_01')<br />
