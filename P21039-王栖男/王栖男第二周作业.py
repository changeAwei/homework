#4. 实现一个简易的计算器，效果如下：
    #（1）. 运行后提示让用户输入一个数字
    #（2）. 提示输入操作符（+ - * /）
    #（3）. 再次提示输入一个数字
    #（4）. 打印计算结果
    #（5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
var = 1
while var ==1:
    m = int(input('Input a number >>> '))
    x = input('input + - * /')
    n = int (input('Input a number>>>'))

    if x == '+':
        print(m + n)
    elif x =='-':
        print(m - n)
    elif x =='*':
        print(m * n)
    else:
        print(x / y)
