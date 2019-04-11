while True:
    a = int(input(''))
    b = input('请输入运算符(+/-/*//)')
    c = int(input(''))
    if b == '+':
        print('{}+{}={}'.format(a,c,a+c))
    elif b == '-':
        print('{}-{}={}'.format(a,c,a-c))
    elif b =='*':
        print('{}*{}={}'.format(a,c,a*c))
    elif b =='/':
        if c == 0:
            print('0不能作为除数,请重新输入')
            continue
        else:
            print('{}/{}={}'.format(a,c,a/c))
    d = input('是否继续（y/n）')
    if d == 'n':
        break
