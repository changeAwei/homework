def compute():
    print('to quit the computer,please input "quit"')

    first = input('please input first number:')
    if first == 'quit':
        exit()
    first = int(first.strip().lstrip('0'))

    opratorlist = ['+', '-', '*', '/']
    operator = input(r'please inpute operator ,one of "+", "-", "*", "/":')
    if operator not in opratorlist:
        print('you can only input one of "+","-","*","/"')
        exit()

    second = input('please input second number:')
    if second == 'quit':
        exit()
    second = int(second.strip().lstrip('0'))

    output = 0
    if operator == '+':
        output = first + second
    elif operator == '-':
        output = first - second
    elif operator == '*':
        output = first * second
    else:
        output = first / second
    print(output)


while True:
    compute()






