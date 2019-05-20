#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2019/5/20 20:33
# @Author : Fly
# @FileName: 第七周作业.py
# @Software: PyCharm

from pathlib import Path
p = Path('/tmp')
def findfile(Path):
    for x in Path.iterdir():  # 拿到子目录及文件的Path对象
        file_change = []
        if x.is_file():  # 判断是否是文件
            if x.suffix == '.htm':  #判断后缀是否是.htm
                file_change.append(str(x.with_suffix('.html')))  # 在列表中添加修改后缀的路径
                print(file_change)
        else:
            findfile(x)  #是文件夹则继续调用函数
findfile(p)
