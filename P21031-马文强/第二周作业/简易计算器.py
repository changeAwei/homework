while True:
    n = int(input('please input number'))
    oper = input('please input "+", "-", "*", "/"')
    m = int(input('please input number'))
    #if input('please input number') == ' ':  这里不知道为什么没有出现判断而是出现了输入框？希望老师解答一下
        #break
    if oper == '+':
        print(n + m)
    elif oper == '-':
        print(n - m)
    elif oper == '*':
        print(n * m)
    elif oper == '/':
        print(n / m) 