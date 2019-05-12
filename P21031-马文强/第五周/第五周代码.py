def logger(fn):
    def wrapper(*args, **kwargs):
        global n
        print("µ⁄{}¥Œ ‰»Î".format(n))
        old = fn(*args, **kwargs)
        return old
    return wrapper
@logger 
def calculator(x, y, operator):
    if operator == '+':
        return x + y
    if operator == '-':
        return x - y
    if operator == '*':
        return x * y
    if operator == '/':
        return x / y
n = 0
while True:
    n = n + 1
    x = int(input('please input first number is '))
    operator = input('please input operator "+", "-", "*", "/" is ')
    if operator == ' ':
        break
    y = int(input('please input second number is '))
    print(calculator(x = x, operator = operator, y = y))