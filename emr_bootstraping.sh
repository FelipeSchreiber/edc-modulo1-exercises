#!/bin/bash
sudo yes | sudo yum install python3-devel
sudo pip3 install cython
sudo pip3 install setuptools --upgrade
sudo pip3 install -U \
    matplotlib \
    pandas
