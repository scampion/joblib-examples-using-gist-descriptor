#!/bin/bash 

echo "install python module"
export PYTHONPATH=.
easy_install --install-dir . joblib
easy_install --install-dir . pyleargist


