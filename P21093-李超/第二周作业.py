while True:
    print("在不退出程序的前提下你不能退出哦！！！")
    num1 = eval(input("请输入一个数字："))
    while True:
        symbol = input("请输入一个运算符(+ - * /)：")
        if symbol not in ('+','-','*','/'):
            continue
        num2 = eval(input("请再输入一个数字"))
        if symbol is '+':
            result = num1 + num2
        elif symbol is '-':
            result = num1 - num2
        elif symbol is '*':
            result = num1 * num2
        elif symbol is '/':
            result = num1 / num2
        print(result)
        break
    else:
        print("请重新输入运算符！！！")
        continue
