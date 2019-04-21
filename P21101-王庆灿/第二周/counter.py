key = 'y'
while key!='q':
    if key == 'y':
        num1 = int(input("Please input the first number: "))
        opera = input("Which operation do you want( + - * / ): ")
        num2 = int(input("Please input the second number: "))
        if opera == '+':
            result = num1 + num2
        elif opera == '-':
            result = num1 - num2
        elif opera == '*':
            result = num1 * num2
        else:
            result = num1 / num2
        print(result)
        key = input("Press 'y' to continue or press 'q' to quit: ")



