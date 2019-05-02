while True:
    a = int(input('>>>'))
    op = input('>>>')# 输入运算符 +,-,*,/中的任意一个
    b = int(input('>>>'))
    def plus(x,y):
        return x+y
    def minus(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        return x/y
    if op == '+':
        print(plus(a,b))
    elif op == '-':
        print(minus(a,b))
    elif op == '*':
        print(multiply(a,b))
    else:
        print(divide(a,b))