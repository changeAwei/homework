#!/usr/bin/env python
#-.-coding:utf-8-.-
print('<<简易计算器>>\n1、输错重输(例如非数字，非运算符等)：\n2、第一个数字空为中断计算')
while True:
    a=b=c='a'
    while not str(a).isdigit() and a !='':
        a=input('请输入第一个数字：')
    if a == '':break
    while b not in ['+','-','*','/']:
        b=input('请输入运算符+-*/：')
    while not c.isdigit():
        c=input('请输入第二个数字：')
    a=int(a)
    c=int(c)
    print('结果如下>>>',end=' ')
    if b=='+':
        print('{}+{}={}'.format(a,c,a+c))
    elif b=='-':
        print('{}-{}={}'.format(a,c,a-c))
    elif b=='*':
        print('{}*{}={}'.format(a,c,a*c))
    else:
        print('{}/{}={}'.format(a,c,a/c))
    print()
