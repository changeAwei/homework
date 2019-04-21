while True:
    a = int(input('>>>'))
    op = input('>>>')# 输入运算符 +,-,*,/中的任意一个
    b = int(input('>>>'))
    if op == '+':
        c = a+b
    elif op == '-':
        c = a-b
    elif op == '*':
        c = a*b
    else:
        c = a/b
    print(c)