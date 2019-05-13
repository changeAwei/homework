### 一、如何为函数定义keyword-only参数（写出个例子即可）？

```python
def person(name, *, age):
    print(name, age)
    
    
person('Tom', age='18') # 调用的时候
```





### 二、什么是LEGB，请解释

```
L: 全称Local, 有函数范围的命名空间
E: 全称Enclosing，
G: 全称Global，有模块范围的命名空间
B: 全称Built-in，有python内建的命名空间

1.命名空间
指的是变量的可见范围，简单的说就是作用的表现形式。
一个变量可以存在多个命名空间内，但是1个命名空间不能存在2个相同的变量；比如：2个班上可以分别有1个李白同学，但是1个班上如果有2个李白同学的话，那就比较尴尬了；而映射到python，就不能允许出现1个命名空间内存在2个相同的变量

2.命名空间的生命周期
所有命名空间都是有生命周期的
* B:对于python内建的命名空间，其生命周期是：python解析器启动创建一直到解析器退出，其生命周期才消亡
* G: 该模块被import的时候创建，解析器退出后，消亡
* L: 函数被调用的时候创建，调用完成后，消亡
* E: 直接外围作用域，简单的说，就是外围嵌套函数的命名空间

3.查找的优先级
Local  >   enclosing  > Global  > Built-in


```

```python
举例
#!/usr/bin/env python
# encoding: utf-8

x = 1 

def foo():
    x = 2 
    def innerfoo():
    #    x = 3                  #此处改动：注释掉
        print 'locals ', x
    innerfoo()
    print 'enclosing function locals ', x

foo()
print 'global ', x

-------结果------
locals  2
enclosing function locals  2
global  1
```



### 三、二叉树的性质

```
1.在第i层上，最多只有 $$ 2^{i-1} $$ 个结点；在深度
2.在深度为k的二叉树，最多有 $$ 2^k -1 $$ 个结点
3.二叉树如果其终端节点数为n0，度数为2的结点为n2，则有n0=n2+1
4.具有 n (n>=0) 个结点的完全二叉树的深度为 $$ log_{2}n＋1 $$
5.高度为n的二叉树，至少有n个结点



其他
1.二叉树不存在度数大于2的节点，即：每个节点最多2颗树
2.二叉树是有序树，左右子树是有顺序的，不能交换顺序；若某个节点只有1个子树，也要确定他是左子树还是右子树
3.二叉树有5种形态：空二叉树、只有1个根节点的树、根节点只有左子树、根节点只有右子树、根节点有左子树和右子树

```



###四、使用本周学习的技术改造第二周的计算器实现，其目标如下：

1. 运行后提示让用户输入一个数字
2. 提示输入操作符（+ - * /）
3. 再次提示输入一个数字
4. 打印计算结果
5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计


6.  尽可能改善用户体验（新需求）

```
#!/usr/bin/python
import sys


def input_number():
    input_num = raw_input('plz input number: ')
    while True:
        if input_num == 'q' or input_num == 'quit':
            sys.exit(0)
        elif input_num == '\n':
            break
        else:
            if input_num.isdigit():
                return input_num
            else:
                input_num = raw_input('plz input number again: ')
                continue



def input_mark_fun():
    marks = ['+','-','*','/']
    in_mark = raw_input('plz input mark [ + - * /] : ')
    while True:
        if in_mark == 'q' or in_mark == 'quit':
            sys.exit(0)
        elif in_mark == '\n':
            break
        else:
            if in_mark in marks:
                return in_mark
            else:
                in_mark = raw_input('plz input mark again [ + - * /]: ')
                continue

def compute_list():
    com_list = []
    while True:
        input_num1 = input_number()
        input_mark = input_mark_fun()
        input_num2 = input_number()
        if input_mark == '+':
            result = int(input_num1) + int(input_num2)
        elif input_mark == '-':
            result = int(input_num1) - int(input_num2)
        elif input_mark == '*':
            result = int(input_num1) * int(input_num2)
        elif input_mark == '/':
            result = int(input_num1) / int(input_num2)

        result_str = "result: {0}{1}{2}={3}".format(input_num1, input_mark, input_num2, result)
        print result_str
        print '[INFO]:input "quit" or "q" to quit,or continue '

    return com_list

compute_list()
```

