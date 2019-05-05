#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : calc.py
@Author: Lint
@Date  : 2019/5/5 17:38
@Vers   :
@Desc  :
使用本周学习的技术改造第二周的计算器实现，其目标如下：
     1. 运行后提示让用户输入一个数字
     2. 提示输入操作符（+ - * /）
     3. 再次提示输入一个数字
     4. 打印计算结果
     5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
     6. 尽可能改善用户体验（新需求）
"""


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


while True:
    num_1 = input("Please input first number or input 'Q/q' quit>>> ")
    if num_1.lower() == "q":
        break
    else:
        num_1 = int(num_1)
    operator = input("""input operator"+,-,*,\">>> """)
    num_2 = int(input('Please input second number:'))
    result = 0
    if operator == '+':
        result = add(num_1, num_2)
    elif operator == '-':
        result = sub(num_1, num_2)
    elif operator == '*':
        result = mul(num_1, num_2)
    elif operator == '/':
        result = div(num_1, num_2)
    print('{}{}{}='.format(num_1, operator, num_2), result)
