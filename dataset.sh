#!/bin/bash 

echo "install python module"
export PYTHONPATH=.
easy_install --install-dir . joblib
easy_install --install-dir . pyleargist

echo "Download and upack dataset"
wget http://people.csail.mit.edu/torralba/code/spatialenvelope/spatial_envelope_256x256_static_8outdoorcategories.zip -O pics.zip
mkdir pics	
unzip pics.zip -d pics/ 
rm pics.zip

echo "cache directory"
mkdir tmp
