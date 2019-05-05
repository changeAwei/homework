

#### 一、什么是杨辉三角和转置矩阵（文字说明即可）？

```
杨辉三角
本质特征：两条斜边的数都为1组成，其余的数都等于它上面两肩的数之和

转置矩阵
本质特征：将矩阵的行和列互换，得到的新矩阵则为转置矩阵
```





#### 二、说明列表和Set集合的相同点和不同点

```
相同点：
a.都是一种可以存储数据的序列

不同点：
a.列表的元素可以重复，set集合中的元素不会出现重复
b.列表中的元素是有序的，set集合中的元素是无序的
```



#### 三、请写出Set集合支持的所有方法及说明（例如：add 向Set集合中添加一个元素）

```
add(ele):向集合中添加新的元素，如果存在就不添加
update(序列)：合并其他序列到此集合中来
remove(ele)：移除1个元素，元素不存在抛出kererror异常
discard(ele):从set中移除1个元素，元素不存在则不抛出异常
union(序列)：返回2个集合的并集，返回的是新的集合；update是就地修改
intersection_update(序列)：获取多个集合的交集并就地修改
difference(序列)：返回和多个集合的差集集合，返回的是新的集合
difference_update(序列)：获取多个集合的差集，就地修改
issubset(other)：判断当前集合是否是另一个集合的子集
s1 < s2：判断s1是否是s2的真子集
issuperset(other)：判断当前集合是否另外1个集合的超集
isdisjoint(other)：判断当前集合和另外集合是否没有交集
```

#### 四、请写出字典支持的所有方法及说明（例如：pop 从字典中移除指定的key并返回其value）

```
D.clear() -> 从字典D中清除所有的元素
D.copy() -> 浅拷贝
D.has_key(k) -> 如果D中的键有k，则返回True，反之返回False
D.items() -> 返回1个列表，元素是：(key1, value2)的二元组
D.keys() -> 返回元素是键的列表
D.values() -> 返回的元素是值的列表
D.pop(k[,d]) -> 弹出指定k的value
D.setdefault(k[,d]) -> 返回k对应的value，如果k没在D里面就自动添加：D[k]=d ，如果d不存在，则默认为None
D.get(k)-> 返回k对应的value

```



#### 五、写出Python内建函数及说明（<https://docs.python.org/3/library/functions.html>）

```
id(object):返回ob的对象的唯一id值，一般为对象在内存中的地址
hash(object):返回ob对象的哈希值
type(ob):返回ob对象的类型
input('xxx')：返回接收用户的输入，并返回1个字符串
print():打印输出
len(ob):判断集合的元素个数
isinstance(obj, class_or_tuple)：判断对象是否是某个类型
issubclass(cls, class_or_tuple)：判断cls是否是属于某个的子类
abs(y):求某个数的绝对值
pow(x,y):等价x*y
sorted(序列)：返回1个新的列表，默认是升序
reversed(序列)：返回1个反转的迭代器
各种类型函数：list() dict() set() 
zip(*itertables):把多个迭代器对象合并在一起，返回1个迭代器
iter(可迭代对象)：把1个可迭代对象封装成迭代器
```

