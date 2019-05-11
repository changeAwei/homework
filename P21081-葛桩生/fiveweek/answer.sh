1. 如何为函数定义keyword-only参数（写出个例子即可）？
{
#这边的x y  是keyword-only参数  与x,y,*args,**kwargs 不一样
#这边x,y 如果不传参会直接报错
def fn(*args,x,y,**kwargs): 
    print(x)
    print(y)
    print(args)
    print(kwargs)

fn(3,4,6,8,x=5,y=10,s=12,w=32)
返回：
5
10
(3, 4, 6, 8)
{'s': 12, 'w': 32}

}
2. 什么是LEGB，请解释
{
LEGB是变量名的解析规则。顺序是Local>Enclosing>Global>Build-in
}
3. 二叉树的性质
{
性质1：二叉树第i层上至多有2^(i-1)个结点(i≥1)
性质2：深度为k 的二叉树，至多有2^k-1个结点(k≥1)
性质3：对任何一棵二叉树中，如果终端结点个数为n0，度数为2的结点数为n2，则n0=n2+1。
性质4：高度为k的二叉树，至少有k个结点
性质5：含有n(n≥1)的结点的二叉树高度至多为n,最小为math.ceil(log2(n+1)) 不小于对数值的最小整数，向上取整
}
4. 使用本周学习的技术改造第二周的计算器实现，其目标如下：
     1. 运行后提示让用户输入一个数字
     2. 提示输入操作符（+ - * /）
     3. 再次提示输入一个数字
     4. 打印计算结果
     5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
     6. 尽可能改善用户体验（新需求） 
{
operator1 = ['+','-','*','/']
while True:
        num1 = input('please input number one:')
        while not num1.strip().isdigit():
            num1 = input('please input number one:')
        operator = input('please input one operator + or  -  ro *  or /:') 
        while operator not in operator1:
            operator = input('please input one operator + or  -  ro *  or /:')
        num2 = input('please input number two:')
        while not num2.strip().isdigit():
            num2 = input('please input number two:') 
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            print('{} + {} = {}'.format(num1,num2,num1+ num2))
        elif operator == '-':
            print('{} - {} = {}'.format(num1,num2,num1-num2))
        elif operator == '*':
            print('{} * {} = {}'.format(num1,num2,num1*num2))
        else:
            print('{} / {} = {}'.format(num1,num2,num1/num2))
        choice = input("是否继续计算（Y/N）").upper()
        if choice == 'Y':
            continue
        else:
            break      
}