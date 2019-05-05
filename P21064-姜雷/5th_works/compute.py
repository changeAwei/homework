#!/usr/bin/env python
# -*- coding: utf-8 -*-


def compute():
    while True:
        print('to quit the computer,please input "quit"')

        first = input('please input first number:')
        if first == 'quit':
            break
        firstnumber = 0 if int(first) == 0 else int(first.strip().lstrip('0'))

        opratorlist = ['+', '-', '*', '/']
        operator = input(r'please inpute operator ,which is one of "+", "-", "*", "/":')
        if operator not in opratorlist:
            print('you can only input one of "+","-","*","/"')
            continue

        second = input('please input second number:')
        if second == 'quit':
            break
        secondnumber = 0 if int(second) == 0 else int(second.strip().lstrip('0'))

        if operator == '+':
            sesult = firstnumber + secondnumber
        elif operator == '-':
            sesult = firstnumber - secondnumber
        elif operator == '*':
            sesult = firstnumber * secondnumber
        else:
            sesult = firstnumber / secondnumber
        print('the sesult is {}'.format(sesult))


compute()
