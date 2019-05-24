#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : Change the file name.py
@Author: Lint
@Date  : 2019/5/22 13:35
@Ver   :
@Desc  :
写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html
"""
from pathlib import Path
import os


def change_name(scr='.htm', des='.html', dir_path='/tmp'):
    f = Path(dir_path).rglob('*' + scr)
    for _ in f:
        os.rename(_, _.with_suffix(des))


change_name()
