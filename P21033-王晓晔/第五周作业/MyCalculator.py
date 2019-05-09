def MyCal(num1,op,num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    return result

while True:
    num1 = input('first number is ')
    if num1.isdigit():
        num1 = int(num1)
    else:
        print('Not a number')
        continue
    op = input('operator is ')
    if op not in ('+-*/'):
        print('Not a operator')
        continue
    num2 = input('second number is ')
    if num2.isdigit():
        num2 = int(num2)
    else:
        print('Not a number')
        continue
    result = MyCal(num1,op,num2)
    print("{} {} {} {} {}".format(num1, op, num2, '=', result))
    flag = input('Continue?[Y/N]')
    if flag not in ('Y','y'):
        break
    continue