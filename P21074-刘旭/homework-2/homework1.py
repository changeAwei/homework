while True:
    x = int(input('Input first number:'))
    operate = input('Input a operate:+,-,*,/:')
    y = int(input('Input a number:'))
    if operate == '+':
        print('{} + {} = {}'.format(x,y,x+y))
    elif operate == '-':
        print('{} - {} = {}'.format(x,y,x-y))
    elif operate == '*':
        print('{} * {} = {}'.format(x,y,x*y))
    elif operate == '/':
        print('{} / {} = {}'.format(x,y,x/y))
    else:
        break