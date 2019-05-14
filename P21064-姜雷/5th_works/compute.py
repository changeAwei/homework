#!/usr/bin/env python
# -*- coding: utf-8 -*-


def compute():
    while True:
        print('to quit the computer,please input "quit"')

        first = input('please input first number:')
        if first == 'quit':
            break
        if int(first) == 0:
            first = 0
        else:
            first = int(first.strip().lstrip('0'))

        operator = input(r'please inpute operator ,one of "+", "-", "*", "/":')
        if operator not in ['+', '-', '*', '/']:
            print('you can only input one of "+","-","*","/"')
            break

        second = input('please input second number:')
        if second == 'quit':
            break
        if int(second) == 0:
            second = 0
        else:
            second = int(second.strip().lstrip('0'))

        if operator == '+':
            output = first + second
        elif operator == '-':
            output = first - second
        elif operator == '*':
            output = first * second
        else:
            output = first / second
        print(output)


compute()
