'''
4. 使用本周学习的技术改造第二周的计算器实现，其目标如下：
     1. 运行后提示让用户输入一个数字
     2. 提示输入操作符（+ - * /）
     3. 再次提示输入一个数字
     4. 打印计算结果
     5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
     6. 尽可能改善用户体验（新需求）
'''

def calculator(num1, oper, num2):
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        result = num1 / num2
    else:
        print('Calculation failure!')
    return result

q = 1
while q:
    print('This is a calculator program!')
    while True:
        num1 = input('Please enter the first number:')
        if num1.isdigit():
            num1 = int(num1)
            break
        else:
            print("This is not numeric types, Please re-enter!")

    while True:
        oper = input('Please enter an operator(+ - * /):')
        if oper not in ('+-*/'):
            print('The oper is wrong, Please re-enter!')
        else:
            break

    while True:
        num2 = input('Please enter the second number:')
        if num2.isdigit():
            num2 = int(num2)
            break
        else:
            print("This is not numeric types, Please re-enter!")
    # result = calculator(num1, oper, num2)
    print('{} {} {} = {}'.format(num1, oper, num2, calculator(num1, oper, num2)))
    q = int(input("Enter '0' to exit, Enter '1' to continue"))
