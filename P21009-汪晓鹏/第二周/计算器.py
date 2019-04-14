q = 1
while q:
    num1 = int(input('Please enter a number:'))
    oper = input('Please enter an operator(+ - * /):')
    num2 = int(input('Please enter a number:'))
    if oper == '+':
        Result = num1 + num2
    elif oper == '-':
        Result = num1 - num2
    elif oper == '*':
        Result = num1 * num2
    elif oper == '/':
        Result = num1 / num2
    else:
        print('Calculation failure!')
        continue
    print('{} + {} = {}'.format(num1,num2,Result))
    q = int(input("Enter '0' to exit, Enter '1' to continue"))
    