#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : re.py
@Author: Lint
@Date  : 2019/5/29 10:05
@Ver   :
@Desc  :
有字符串”not 404 found 张三 99 深圳”，使用正则过滤掉英文和数字，最终得到”张三 深圳”
"""
import re

str1 = "not 404 found 张三 99 深圳"
lst1 = str1.split(' ')
lst2 = re.findall('[a-zA-Z]+|\d+\.?\d*', str1)
for i in lst2:
    if i in lst1:
        lst1.remove(i)
new_str = ' '.join(lst1)
print(new_str)
