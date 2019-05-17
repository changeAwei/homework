# -*- coding: utf-8 -*-
# @Time  : 2019/5/5 19:46
# @Author : xm11211
# @FileName: calc.py
# @Software: PyCharm
def calc():
    while True:
        num1 = int(input('Please intput a num:'))
        operator = (input('Please intput a operator(+ - * /):'))
        num2 = int(input('Please intput a num:'))
        if operator == '+':
            print('{} * {} = {}'.format(num1,num2,num1 + num2))
        elif operator == '-':
            print('{} - {} = {}'.format(num1,num2,num1 - num2))
        elif operator == '*':
            print('{} * {} = {}'.format(num1,num2,num1 * num2))
        elif operator == '/':
            print('{} / {} = {}'.format(num1,num2,num1 / num2))
        remind = input("Enter 'q'exit,enter other character to continue:")
        if remind == 'q':
            break
        else:
            continue
calc()