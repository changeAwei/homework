while True:
    x = int(input('Enter a number:').strip())
    o = input('Enter operator:')
    y = int(input('Enter another number:').strip())
    if o=='+':
        print('x + y = {}'.format(x + y))
    elif o=='-':
        print('x - y = {}'.format(x - y))
    elif o=='*':
        print('x * y = {}'.format(x * y))
    elif o=='/':
        print('x / y = {}'.format(x / y))
    else:
        break
