#!/usr/bin/env python
# -*- coding: utf-8


import argparse


parser = argparse.ArgumentParser(prog='cat', description='view file contents')
parser.add_argument('file', nargs='*',help='file to view')
parser.add_argument('-n','--number',action='store_true',help='number all output lines')

args = parser.parse_args()


# print(args)
# parser.print_help()


def view(file_list, n=False):
    if not n:
        for file in file_list:
            for line in open(file):
                print(line)
    else:
        num = 1
        for file in file_list:
            for line in open(file):
                print('\t' + str(num) + '  ' + line)
                num += 1


view(args.file, args.number)
