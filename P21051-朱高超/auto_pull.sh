#!/bin/bash

PY_PATH=/Users/`whoami`/Documents/Code/mage.py/homework/P21051-朱高超

cd ${PY_PATH}
git pull
git add .
git commit -m "auto git $1"
git push -u origin master



