def calculator(x,operator,y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
while True:
    x = int(input("输入第一个数字: "))
    operator = str(input("输入运算符号('+-*/'):"))
    if operator not in '+-*/':
        print('不识别的运算符')
        continue
    y = int(input("输入第二个数字: "))
    if operator =='/' and y == 0 :
        print('非法的输入')
        continue
    print('{}{}{}={}'.format(x, operator, y, calculator(x, operator, y)))
    remind = int(input("Enter '0' to exit, Enter '1' to continue"))
    if remind == 0:
        break
    else:
        continue
