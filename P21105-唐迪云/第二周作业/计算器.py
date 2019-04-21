while True:
    num1 = int(input('please input first number：'))
    operator = (input('please input operator(+ - * /):'))
    num2 = int(input('please input second number：'))
    if operator == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) - int(num2)
    elif operator == '*':
        result = int(num1) * int(num2)
    elif operator == '/':
        result = int(num1) / int(num2)
    print('{}{}{}='.format(num1,operator,num2),result)

