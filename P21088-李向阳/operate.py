while True:
    x = int(input('Input a first num:'))
    operate = int(input('Input a operate:+,-,*,/:'))
    y = int(input('Input a second num:'))
    if operate == '+':
        print('{} + {} = {}'.format(x,y,x+y))
    if operate == '-':
        print ('{} - {} = {}'.format(x,y,x-y))
    if operate == '*':
        print('{} * {} = {}'.format(x,y,x*y))
    if operate == '/':
        print('{} / {} = {}'.format(x,y,x/y))
    else:
        break
