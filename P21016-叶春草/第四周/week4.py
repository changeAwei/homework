#!/usr/bin/env python
#coding=utf-8
'''
1. 什么是杨辉三角和转置矩阵（文字说明即可）？
2. 说明列表和Set集合的相同点和不同点。
3. 请写出Set集合支持的所有方法及说明（例如：add 向Set集合中添加一个元素）
4. 请写出字典支持的所有方法及说明（例如：pop 从字典中移除指定的key并返回其value）
5. 请写出Python内建函数及说明（参考：https://docs.python.org/3/library/functions.html）
'''

print('''
1、杨辉三角是指一个数字组成的等腰三角形，首尾是1，其他数字都是上一行两边数字之和。
   转置矩阵是指将数字组成的矩阵，行、列互换。
2、列表与set集合的：
   相同点：都是数据容器，可迭代，可修改
   不同点：列表有序，能索引，能重复，在存储中占用连续空间
3、set支持的所有方法：
  s.add()	添加元素入集合（如果已经存在则集合不改变）
  s.clear()	清空集合
  s.copy()	复制集合
  s.difference(s1)	差集，在s中存在而不在s1中的集合
  s.discard()	丢弃一个元素（元素不存在则不处理）
  s.remove()	丢弃一个元素，元素必须存在
  s.intersection()	交集，返回两个集合都存在的元素
  s.intersection_update()	反正交集并修改自身
  s.isdisjoint()	两集合无相同元素则返回True
  set1.issubset(set2)	set1是否是set2的子集
  set1.issuperset(set2)	 set2是否是set1的子集
  s.pop()	随机移除元素
  s.symmetric_difference()	返回两个集合中不重复的元素集合
  s.symmetric_difference_update()	修改成两个集合不不重复的元素集合
  s.union()	并集
  s.update()	给集合添加元素
4、字典支持的所有方法：
  d.clear()	清空元素
  d.copy()	复制字典
  dict.fromkeys(iterable, value=None, /)	创建新字典，可迭代元素为key,value为字义的value
  d.get(k[,d])	获取k对应的value，无k则返回默认值d（无定义则是None）
  d.items()	返回d的键值对
  d.keys()	返回d的键
  d.values()	返回d的值
  d.pop(k[,d])	移除一个k并返回v，如果k不存在时则返回d(如果d无设置则报错)
  d3.popitem()	随机移除键值，如果为空则报错
  d.setdefault(k[,d])	跟get类似，如果不存在则会添加入字典
  d1.update(d2)	把d2的键值更新至d1
5、常用的内建函数如下：
##类型转换或初始化：
set()	集合
dict()	字典
frozenset()	返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
bin()	将其他进制转换成二进制
hex()	转换成十六进制的数字
oct()	转换成八进制
int()	将一个字符串或数字转换为整型
str()	转换成字符串
tuple()		元组
zip()		将对象中对应的元素打包成一个个元组
list()		列表
iter()		生成迭代器
type()		查看类型
format()	返回格式化后的字符串

##数值类
max()	查看最大值
min()	查看最小值
sum()			求和
float()			将整数和字符串转换成浮点数
range()		生成数字序列
sorted()		排序
round()	四舍六入五取偶
divmod()	返回商跟余数

##编码相关
bytes()		返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本
chr()		用一个整数作参数，返回一个对应的字符
compile()	将一个字符串编译为字节代码

##其他
all()	判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
any()	判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
hash()		计算哈希值
id()	查看内存地址
input()		在交互中取值
bool()		查看一个值的布尔值
help()	查看函数或模块用途的详细说明
isinstance()	判断类型
print()			打印
setattr()	setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。
open()		打开文件
globals()	以字典类型返回当前位置的全部全局变量
locals()	以字典类型返回当前位置的全部局部变量
callable()	判断是否可调用

len()		查看长度
next()		返回迭代器中的下一个值
slice()		切片取值
super()		转换成大写
vars()		返回对象object的属性和属性值的字典对象。
hasattr()	判断对象是否包含对应的属性
getattr()	用于返回一个对象属性值
property()	在新式类中返回属性值
enumerate()	用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
eval()		执行shell命令
exec()	执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码
bytearray()	返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
filter()	过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换
map()		根据提供的函数对指定序列做映射。
reversed()	反转
''')
