while True:
    num1 = int(input('first number is '))
    op = input('operator is ')
    num2 = int(input('second number is '))
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print('Wrong Operator')
        break
    print(('result is ') + str(result))
    flag = input('Continue?[Y/N]')
    if flag != 'Y':
        break
    continue