#### Vowpal Wabbit guide

##### Install
sudo apt-get install libboost-all-dev<br />
./configure --with-boost-libdir=/usr/lib/x86_64-linux-gnu​ (needs to be passed the location on Boost)<br />
make<br />
sudo make install (this fails)<br />
make test (also fails)<br />
vw -- version<br />

