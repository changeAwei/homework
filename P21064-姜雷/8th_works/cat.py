#!/usr/bin/env python
# -*- coding: utf-8


import argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='cat', description='view file contents')
parser.add_argument('file', nargs='*',help='file to view')
parser.add_argument('-n','--number',action='store_true',help='number all output lines')

args = parser.parse_args()


# print(args)
# parser.print_help()


def view(file_list, n=False):
    if not n:
        for file in file_list:
            p = Path(file)
            if not p.absolute().is_file():
                print('{} must be a file'.format(file))
            else:
                with p.open() as f:
                    for line in f:
                        print(line)
    else:
        num = 1
        for file in file_list:
            p = Path(file)
            if not p.absolute().is_file():
                print('{} must be a file'.format(file))
            else:
                with p.open() as f:
                    for line in f:
                        print('\t' + str(num) + '  ' + line)
                        num += 1


view(args.file, args.number)
