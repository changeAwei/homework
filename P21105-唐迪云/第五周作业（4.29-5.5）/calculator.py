#想多参考参考他人的，集思广益，新的需求
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
    remind = input("Enter 'q'exit,enter other character to continue:")
    if remind == 'q':
        break
    else:
        continue