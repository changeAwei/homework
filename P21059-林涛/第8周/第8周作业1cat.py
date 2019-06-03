#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : cat.py
@Author: Lint
@Date  : 2019/6/2 19:08
@Ver   :
@Desc  :
cat命令基本功能实现，实现参数n，可以添加路径
"""
import argparse
from pathlib import Path


def cat(file_name: str, dis_num=False, path=False):
    if not path:
        p = Path(file_name)
    else:
        p = Path(path, file_name)
    with open(p, 'r') as f:
        for num, v in enumerate(f):
            num += 1
            if dis_num:
                print(num, v, end='')
            else:
                print(v, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='cat',
        description='Concatenate FILE(s), or standard input, to standard output.',
        add_help=True,
    )
    parser.add_argument('file_name', help='file name')
    parser.add_argument('path', nargs='?', default='.', help='filepath')
    parser.add_argument('-n', '--number', dest='dis_num', action='store_true', help='number all output lines')
    args = parser.parse_args()  # '/etc'.split()

    # parser.print_help()
    # print(args.file_name, args.dis_num, args.path)
cat(args.file_name, args.dis_num, args.path)
