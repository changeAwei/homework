# 1. 如何为函数定义keyword-only参数（写出个例子即可）？
"""在一个星号参数后、或者一个可变位置参数后的形参
函数调用时必须使用关键字参数传参
调用时如果没有默认值，则必须传递实参，否则将抛出TypeError缺少keyword-only参数异常"""
james = {'name': 'James', 'age': 20}
bob = {'name': 'Bob', 'age': 22}
def compare(a, b, *, key):
    return a[key] > b[key]
# 关键字key在星号*后，当我们以位置顺序调用时：
# 会得到错误：
# TypeError: compare() takes 2 positional arguments but 3 were given
try:
    compare(james, bob, 'age')
except Exception as e:
    print(e)

# 而只有以：
print(compare(james, bob, key='age'))
# 才会正确返回：False

# 2. 什么是LEGB，请解释
"""
LEGB就是用来规定命名空间查找顺序的规则。
LEGB规定了查找一个名称的顺序为: local-->enclosing function locals-->global-->builtin
"""
# 3. 二叉树的性质
"""
性质1：二叉树第i层上的结点数目最多为 2{i-1} (i≥1)。
性质2：深度为k的二叉树至多有2{k}-1个结点(k≥1)。
性质3：包含n个结点的二叉树的高度至少为log2 (n+1)。
性质4：在任意一棵二叉树中，若终端结点的个数为n0，度为2的结点数为n2，则n0=n2+1。
"""
# 4. 使用本周学习的技术改造第二周的计算器实现，其目标如下：
#      1. 运行后提示让用户输入一个数字
#      2. 提示输入操作符（+ - * /）
#      3. 再次提示输入一个数字
#      4. 打印计算结果
#      5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
#      6. 尽可能改善用户体验（新需求）
while True:
    try:
        print()
        oneNum = int(input("请输入一个数字："))
        operator = ''
        while True:
            operator = input("请输入(+ - * /)：")
            if operator=='+' or operator=='-' or operator=='*' or operator=='/':
                break
            else:
                print()
                print('请输入正确的运算符：')
                continue
        print()
        twoNum = int(input("请输入第二个数字："))

        if operator =="+":
            print(oneNum+twoNum)

        if operator =="-":
            print(oneNum-twoNum)

        if operator =="*":
            print(oneNum*twoNum)

        if operator =="/":
            print(oneNum/twoNum)
    except:
        print('\n','输入有误')
        pass
    print()
    quit = input("Y(y)继续|其它退出").upper()
    if quit == 'Y':
        continue
    else:
        break