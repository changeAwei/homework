def calculator(num1, oper, num2):
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        result = num1 / num2
    else:
        print('Calculation failure!')
    return result

q = 1
while q:
    while True:
        num1 = input('Please enter the first number:')
        if num1.isdigit():
            num1 = int(num1)
            break
        else:
            print("This is not numeric types, Please re-enter!")

    while True:
        oper = input('Please enter an operator(+ - * /):')
        if oper not in ('+-*/'):
            print('The oper is wrong, Please re-enter!')
        else:
            break

    while True:
        num2 = input('Please enter the second number:')
        if num2.isdigit():
            num2 = int(num2)
            break
        else:
            print("This is not numeric types, Please re-enter!")
    # result = calculator(num1, oper, num2)
    print('{} {} {} = {}'.format(num1, oper, num2, calculator(num1, oper, num2)))
    q = int(input("Enter '0' to exit, Enter '1' to continue"))