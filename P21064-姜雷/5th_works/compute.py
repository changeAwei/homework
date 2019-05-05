#!/usr/bin/env python
# -*- coding: utf-8 -*-


def compute():
    opratorlist = ['+', '-', '*', '/']
    while True:
        print('to quit the computer,please input "quit"')

        first = input('please input first number:')
        if first == 'quit':
            break
        first = 0 if int(first) == 0 else int(first.strip().lstrip('0'))

        operator = input(r'please inpute operator ,which is one of "+", "-", "*", "/":')
        if operator not in opratorlist:
            print('you can only input one of "+","-","*","/"')
            continue

        second = input('please input second number:')
        if second == 'quit':
            break
        second = 0 if int(second) == 0 else int(second.strip().lstrip('0'))

        if operator == '+':
            sesult = first + second
        elif operator == '-':
            sesult = first - second
        elif operator == '*':
            sesult = first * second
        else:
            sesult = first / second
        print('the sesult is {}'.format(sesult))


compute()
