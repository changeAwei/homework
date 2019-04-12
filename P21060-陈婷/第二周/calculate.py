#no.1   char
print("welcome to calculate,if you want to quit, press 'q' anywhere!")
isquit = True                                                                #在第二次输入、第三次输入时，一旦输入'q'，退出循环
while isquit:
    a = input('please first num>>:').strip()
    if a == 'q': break                                                       #第一次输入时，输入q直接退出所有循环
    a = a.lstrip('0')  if a.lstrip('0') else '0'                             #判断用户是否输入全部为‘0’，还是左边有‘0’的字符串
    flag = True                                                              #用户合法输入第二次，第三次后，跳出第二、三个循环，重新进入第一次循环。
    if a.isdigit():
        while True and flag  :
            b = input('please input "+" or "-" or "*" or "/" >>:').strip()
            if b == 'q' :  isquit  = flag = False
            if b == '+' or b == '-' or b == '*' or b == '/':
                while True and flag:
                    c = input('please input other num>>:').strip()
                    if c == 'q':  isquit = flag = False
                    c = c.lstrip('0') if c.lstrip('0') else '0'
                    if c.isdigit():
                        if b == '+': print(a,b,c,'=',int(a) + int(c))
                        elif b == '-': print(a, b, c, '=', int(a) - int(c))
                        elif b == '*': print(a, b, c, '=', int(a) * int(c))
                        elif c == '0':                                       #用户输入'/ '，且 被整除数为'0'。则提示重新输入
                            print('division by zero,please reinput')
                            continue
                        else:
                            print(a, b, c, '=', int(a) / int(c))
                        flag = False
                    else:
                        continue
            else:
                continue
    else:
        continue


