#### 一、简要说明Python垃圾回收机制
##### python垃圾回收引入计数（reference counting）的机制为主，标记清除和分代收集为辅的策略
 ###### 1.引入计数（reference counting）的原理
 > 每个对象维护1个obj_ref的字段，用来记录当前对象被调用的次数，每当新的引用指向该对象的时候（当对象被调用增加1次的时候），obj_ref自增1；当对象引用失效的时候，obj_ref自减1，一旦对象的引用obj_ref字段为0的时候，该对象就会被回收，对象占用的内存空间就会被释放
    优势：一旦没有被引用，内存就释放掉了
    劣势：需要额外的空间维护引用计数；此外，还不能解决对象的循环引用的问题
    
    
##### 2.标记清除（Mark-Sweep）-- 基于追踪回收计数实现的垃圾回收算法
 >分2个阶段
 a.GC会把所有的【活动对象】都打上标记
 b.GC把所有的【非活动对象】（没有标记的对象）进行回收
 于是问题来了，怎么区分和判断【活动对象】与【非活动对象】？
 1）对象之间通过引用关系（指针）连接在一起，构成1个有向图
 2）从根对象出发，能直达的则属于【活动对象】；否则，属于【非活动对象】
 根对象就是全局变量、调用栈、寄存器
 
 
 ##### 3.分代回收
 > python将对象根据存活时间划分为不同的集合，每个集合即为1代，总共将内存分成了3代：年轻代、中年代、老年代
 垃圾回收的频率也随着代数的增加而减少
 新创建的对象被分为年轻代，当年轻代的链表，当到上限的时候，就会触发垃圾回收机制，将可回收的对象回收掉，不可回收的则转移到中年代；老年代也是如此
 
 
参考链接：https://testerhome.com/topics/16556
        
#### 二、什么是斐波那契数列、素数、质数和猴子吃桃问题（文字说明即可）？
##### 1） 斐波拉切数列

>   x =1 或者 2的时候，f(x)=1
   x > 2的时候，f(x) = f(x-1) + f(x-2)
   除了第1项和第2项，后面的所有的每一项都是它的前2项之和
   这样的数列被称为菲波那切数列
    
##### 2） 素数或者质数
> 只能被自身和1整除的自然数

##### 3） 猴子偷桃问题
>  问题：猴子第1天摘了若干个桃子，当即吃了一半，还不解馋，又多吃了1个；第2天，吃了一半，不过瘾又多吃了1个;....一直到第10天再想吃的时候，只剩1个桃子；请问第1天总共有多少个桃子
>  思路：
>    f(10) = 1
>    f(n) = 2 * f(n+1) + 2






#### 三、 请写出列表支持的所有方法及说明（例如: append 向列表末尾添加元素）
>  |  append(...)
 |      L.append(object) -- append object to end
 |      给列表增加1个元素
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
        返回元素在列表中出现的次数
 |
 |  extend(...)
 |      L.extend(iterable) -- extend list by appending elements from the iterable
 |      通过拓展列表添加元素
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
         返回元素在列表中出现的第1索引
 |
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
        在指定索引的前面插入元素
 |
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
        弹出列表中的最后1个元素
 |
 |  remove(...)
 |      L.remove(value) -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
        移除列表中的某个元素
 |
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |      将列表元素反序
 |  sort(...)
 |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
 |      cmp(x, y) -> -1, 0, 1
        将列表进行排序


#### 四、实现一个简易的计算器，效果如下
> （1）. 运行后提示让用户输入一个数字
    （2）. 提示输入操作符（+ - * /）
    （3）. 再次提示输入一个数字
    （4）. 打印计算结果
    （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
    
    
```
#!/usr/bin/python
import sys

def compute():
	input_num1  =raw_input('plz input number : ')
	while True:
            if input_num1 == 'quit':
                sys.exit(0)
	    if len(input_num1) != 0 :
		break
	    else:
		input_num1 =raw_input('plz input number : ')


	input_mark  =raw_input('plz input mark(+ - * /) : ')
	mark_list = ['+','-','*','/']
	while True:
            if input_mark == 'quit':
                sys.exit(0)
	    if len(input_mark) != 0 and input_mark in mark_list:
		break
	    else:
		input_mark  =raw_input('plz input mark(+ - * /) : ')



	input_num2  =raw_input('plz input number : ')

	while True:
            if input_num2 == 'quit':
                sys.exit(0)
	    if len(input_num2) != 0 :
		break
	    else:
		input_num2 =raw_input('plz input number : ')

	if input_mark == '+':
	    result = int(input_num1) + int(input_num2)
	elif input_mark == '-':
	    result = int(input_num1) - int(input_num2)
	elif input_mark == '*':
	    result = int(input_num1) * int(input_num2)
	elif input_mark == '/':
	    result = int(input_num1) / int(input_num2)

	print 'result:',result
        print '[INFO]:input "quit" to quit,or continue '

while True:
    compute()
    
    
```
