#!/usr/bin/env python
'''
1. 如何为函数定义keyword-only参数（写出个例子即可）？
2. 什么是LEGB，请解释
3. 二叉树的性质
4. 使用本周学习的技术改造第二周的计算器实现，其目标如下：
     1. 运行后提示让用户输入一个数字
     2. 提示输入操作符（+ - * /）
     3. 再次提示输入一个数字
     4. 打印计算结果
     5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
     6. 尽可能改善用户体验（新需求） 
	 
	 
‘’‘1、如果在一个星号参数后，或者一个位置可变参数后，出现普通的参数，实际上已经不是普通的参数了，而是keyword-only参数，定义时需要指定参数名。举例：’‘’
#!/usr/bin/env python
def keyword1(*,x,y):
  print('x is %s,y is %s' % (x,y))

def keyword2(*args,x,y):
  print('x is %s,y is %s,args is %s' % (x,y,args))

keyword1(x=3,y=4)
keyword2(1,2,3,4,5,x=3,y=4)

2、LEGB是指函数寻找变量的顺序，由近及远，L指local，局部变量；E指Enclosed，是指多个嵌套函数中，外面那层（非全局）的变量，G是global全局变量，B是building内置变量。

3、	(1)在二叉树的第i层至多有2^(i-1)个结点（i>=1）
	(2)在二叉树的第i层上至多有2^(i-1)个节点（k>=1）
	(3)对任何一棵二叉树T，如果其终端节点数为n0,度数为2的节点为n2,则有n0=n2+1
	(4)具有n个结点的完全二叉树的深度为int(log2n)+1或者math.ceil(log(n+1))
	(5)如果有一棵n个结点的完全二叉树(深度为性质4) , 结点按照层序编号
	如果i=1 ,则结点i是二叉树的根，无双亲
	如果i>1，则其双亲是int(i/2) ,向下取整。就是子节点的编号整除2得到的就是父结点的编号。父结点如果是i,那么左孩子结点就是2i ,右孩子结点就是2i+1。
    如果2i>n,则结点i无左孩子,即结点i为叶子结点;否则其左孩子结点存在编号为2i。
    如果2i+1>n,则结点i无右孩子,注意这里并不能说明结点没有左孩子;否则右孩子结点存在编号为2i+1。
	
	#!/usr/bin/env python
'''
def num(number):
  while True:
    i=input('    %s number : ' % number)
    if i.isdigit():
        return i

def ope():
  while True:
    i=input('    operator (+-*/) : ')
    if i == "+" or i == "-" or i == "*" or i == "/":
        return i


a=num('first')+ope()+num('second')
print(a+'=',end='')
print(eval(a))
