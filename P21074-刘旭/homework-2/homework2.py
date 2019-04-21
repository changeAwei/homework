while True:
    x = int(input('Input first number:'))
    operator = input('Input a operate:+,-,*,/:')
    y = int(input('Input a number:'))
    if operator == '+':
        print('{} + {} = {}'.format(x,y,x+y))
    elif operator == '-':
        print('{} - {} = {}'.format(x,y,x-y))
    elif operator == '*':
        print('{} * {} = {}'.format(x,y,x*y))
    elif operator == '/':
        print('{} / {} = {}'.format(x,y,x/y))
    else:
        break