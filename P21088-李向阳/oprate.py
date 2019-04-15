n = 0
while n == 0:
    a = int(input('Input a num:'))
    b = input('Input a operate: + - * /')
    c = int(input('Input a num:'))
    if b ==' +':
        print(a+c)
    if b == '-':
        print(a-c)
    if b == '*':
        print(a*c)
    if b == '/' and c > 0 or c < 0:
        print(a/c)
    else:
        break
