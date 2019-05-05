def calculator(*args):
    x,o,y = args
    result = 0
    if o=='+':
        result = x + y
    elif o=='-':
        result = x - y
    elif o=='*':
        result = x * y
    elif o=='/':
        result = x / y
    return result

while True:
    tup = ('+', '-', '*', '/')
    x = input('Enter a number:').strip()
    if x=='q':break
    o = input('Enter operator like +-*/:').strip()
    if o == 'q': break
    y = input('Enter another number:').strip()
    if y == 'q': break

    if x.isnumeric() and y.isnumeric() and o in tup:
        x = int(x)
        y = int(y)
        result = calculator(x, o, y)
        print('{} {} {} = {}'.format(x,o,y,result))
    else:
        print('Illegal input')
        continue
