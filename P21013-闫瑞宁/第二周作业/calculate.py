while True:
    num1:str = input('please input a number:')
    if num1.isnumeric():
        num1 = eval(num1)
    else:
        print('wrong input')
    operator = input('please input an operator(+ - * /):')
    operation = ['+', '-','*','/']
    if operator in operation:
        if operator == operation[0]:
            num2: str = input('please input another number:')
            if num2.isnumeric():
                num2 = eval(num2)
            else:
                print('wrong input')
            print(num1 + num2)

        if operator == operation[1]:
            num2: str = input('please input another number:')
            if num2.isnumeric():
                num2 = eval(num2)
            else:
                print('wrong input')
            print(num1 - num2)

        if operator == operation[2]:
            num2: str = input('please input another number:')
            if num2.isnumeric():
                num2 = eval(num2)
            else:
                print('wrong input')
            print(num1 * num2)


        if operator == operation[3]:
            num2: str = input('please input another number:')
            if num2.isnumeric():
                num2 = eval(num2)
            else:
                print('wrong input')
            print(num1 / num2)