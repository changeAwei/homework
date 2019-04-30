#/usr/bin/env 
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

'''

#1、keyword-only参数必须放在位置参数后面，参数示例(关键字传参)
# def fn(a,*args,b):
#     return a+b ,args
# print(fn(3,2,1,b=2))

#2、什么是LEGB
"""
  LOCAL: 这个作用域在当前所在命名空间，函数参数也属于命名空间的变量
  Enclosed：嵌套函数结构中的外部嵌套函数的命名空间（闭包中常见）
  Globals：全局变量，函数定义所在模块的命名空间
  Builtins：内建模块的命名空间
"""

# d = 10 #全局变量模块内的命名空间Globals
# def fn1(a=1): #a是fn1的本地命名空间里的变量LOCAL
#     global d
#     print(d-a)
#     def inner():
#         print(d+a) #这里的d 和a 都用到了外层的变量 Enclosed
#     return inner()
#
# print(fn1()) #print 是内建的模块命名空间Builtins

#3、二叉树的性质
"""
1、树中的节点最多有俩颗树木
2、二叉树的子树有左右之分，左子树、右子树
3、二叉树的子树只有一颗，也要分左右
4、在非空的二叉树的i层上，至多有2**i-1个节点（）i>=1

满二叉树：
1、叶子节点只能出现在最下面一层
2、非叶子节点度一定是2
3、在同样深度的二叉树中，满二叉树的节点数最多，节点个数是：2**n -1 ，其中n是数的深度（也叫几层）
完全二叉树：
1、除了最后一层前面挂满了节点，前面的层于满二叉树一样
2、最大深度的节点是从左向右依次排列的
"""

#4、函数计算机


def get_input():
    input_str = input('>>>>')
    return input_str

def calc(a,b):
    ab_sum = a+b
    ab_difference =a-b
    ab_product = a*b
    ab_quoient = a/b
    return {'sum':ab_sum,'diff':ab_difference,'pro':ab_product,'quo':ab_quoient}

def run():
    print('第一次输入')
    def one(a=int(get_input())):
        print('第二次输入')
        def tow(b=int(get_input())):
            def oper():
                print('输入运算符/或者其他的重新输入')
                run_oper=calc(a,b)
                c = get_input()
                if c == '+':
                    print(run_oper.get('sum'))
                elif c =='-':
                    print(run_oper.get('diff'))
                elif c =='*':
                    print(run_oper.get('pro'))
                elif c == '/':
                    print(run_oper.get('quo'))
                else:
                    run()
            return oper()
        return tow()

    return one()

print(run())
