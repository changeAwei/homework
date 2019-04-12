"""
实现一个简易的计算器，效果如下：
    （1）. 运行后提示让用户输入一个数字
    （2）. 提示输入操作符（+ - * /）
    （3）. 再次提示输入一个数字
    （4）. 打印计算结果
    （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
"""

while True:
    num_1 =  input("Please input first number or input 'Q/q' quit>>> ")
    if num_1.lower() == "q":
        break
    operator =  input("""input operator"+,-,*,\">>> """)
    num_2 =  input('Please input second number:')
    result = 0
    if operator == '+':
        result = int(num_1) + int(num_2)
    elif operator == '-':
        result = int(num_1) - int(num_2)
    elif operator == '*':
        result = int(num_1) * int(num_2)
    elif operator == '/':
        result = int(num_1) / int(num_2)
    print('{}{}{}='.format(num_1,operator,num_2),result)