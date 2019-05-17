#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2019/5/5 20:32
# @Author : Fly
# @FileName: 第五周作业.py
# @Software: PyCharm
def calculator(num1,operator,num2):  # 传入数值及运算符,并计算
    if operator == '+':
        print('{}+{}={}'.format(num1, num2, num1 + num2))
    elif operator == '-':
        print('{}-{}={}'.format(num1, num2, num1 - num2))
    elif operator == '*':
        print('{}*{}={}'.format(num1, num2, num1 * num2))
    elif operator == '/':
        print('{}/{}={}'.format(num1, num2, num1 / num2))
    return judge()
def zero():# 除数为0的特殊情况
    print('0不能作为除数,请重新输入')
    return entry()
def judge():# 是否继续的特殊情况
    decide = input('是否继续（y/n）')
    if decide == 'n':
        print("""已退出""")
    else:
        return entry()
def entry():# 输入
    num1 = int(input('请输入数字'))
    operator = input('请输入运算符(+/-/*//)')
    num2 = int(input('请输入数字'))
    if operator =='/' and num2 == 0:
        return zero()
    return calculator(num1,operator,num2)

entry()
