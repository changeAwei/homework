1. 什么是杨辉三角和转置矩阵（文字说明即可）？
{杨辉三角：每个数等于它上方两数之和，第n行的数字有n项，第n行的m个数可表示为 C(n-1，m-1)，即为从n-1个不同元素中取m-1个元素的组合数，每个数字等于上一行的左右两个数字之和
转置矩阵：是将矩阵的行列互换得到新矩阵
}
2. 说明列表和Set集合的相同点和不同点。
{
相同点：可迭代，元素可变
不同点：列表----->元素可以是任意对象，可以重复可索引
        set集合-->元素不可重复且必须是可哈希，不可索引
}
3. 请写出Set集合支持的所有方法及说明（例如：add 向Set集合中添加一个元素）
{
add(elem) 增加一个元素到set中，如果元素存在，什么都不做，set和list无法作为add参数直接加入
update(*others) 合并其他元素到set集合中来，参数others必须是可迭代对象，就地修改
remove(elem) 从set中移除一个元素，元素不存在，抛出KeyError异常
discard(elem) 从set中移除一个元素，元素不存在，什么都不做
pop() 移除并返回任意的元素,空集返回KeyError异常
clear() 移除所有元素
}
4. 请写出字典支持的所有方法及说明（例如：pop 从字典中移除指定的key并返回其value）
{
dict(**kwargs)使用name=value对初始化一个字典
dict(iterable, **kwarg) 使用可迭代对象和name=value对构造字典，不过可迭代对象的元素必须是一个二元结构
dict(mapping, **kwarg) 使用一个字典构建另一个字典
fromkeys(iterable, value) 使用可迭代对象构造字典
d[key] 返回key对应的值value,key不存在抛出KeyError异常
update([other]) 使用另一个字典的kv对更新本字典, key不存在，就添加,key存在，覆盖已经存在的key对应的值,就地修改
d[key] = value 将key对应的值修改为value,key不存在添加新的kv对
get(key[, default]) 返回key对应的值value, key不存在返回缺省值，如果没有设置缺省值就返回None
setdefault(key[, default]) 返回key对应的值value,key不存在，添加kv对，value设置为default，并返回default，如果default没有设置，缺省为None
pop(key[, default]), key存在，移除它，并返回它的value,key不存在，返回给定的default,default未设置，key不存在则抛出KeyError异常
popitem() 移除并返回一个任意的键值对,字典为empty，抛出KeyError异常
clear() 清空字典
}
5. 请写出Python内建函数及说明（参考：https://docs.python.org/3/library/functions.html）
{
abs()返回数字的绝对值
all()用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
any()用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，否则返回 True。	
bin()返回一个整数 int 或者长整数 long int 的二进制表示。
bool()将给定参数转换为布尔类型，如果没有参数，返回False。	
bytearray()	方法返回一个新字节数组。
bytes()	返回一个新的 bytes 对象。
callable()检查一个对象是否是可调用。
chr()给一个一定范围的整数返回对应的字符
compile()将一个字符串编译为字节代码
complex()创建一个复数
delattr()删除属性
dict()创建一个字典
dir()不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
divmod()等价于tuple (x//y, x%y)
enumerate()枚举，迭代一个序列，返回索引数字和元素构成的二元组
eval()执行一个字符串表达式，并返回表达式的值
exec()执行储存在字符串或文件中的 Python 语句
filter()过滤序列
float()	转换成浮点数
format()格式化函数
frozenset()	一个冻结的集合
getattr()返回一个对象属性值
globals()以典类型返回当前位置的全部全局变量
hasattr()	判断对象是否包含对应的属性
hash()返回一个对象的哈希值
help()帮助函数，查看详细说明
hex()转换为 16 进制数
id()返回对象的唯一标识，CPython返回内存地址
input()接收用户输入，返回一个字符串
int()转换为整型
isinstance()判断对象obj是否属于某种类型或者元组中列出的某个类型
issubclass()判断类型cls是否是某种类型的子类或元组中列出的某个类型的子类
iter()生成迭代器
len()返回一个集合类型的元素个数
list()转换为列表
locals()以字典类型返回当前位置的全部局部变量
map()对指定序列做映射
max()最大值
memoryview()返回给定参数的内存查看对象
min()最小值
next()返回迭代器的下一个项目
object()基类
oct()转换成8进制字符串
open()打开一个文件，并返回文件对象
ord()返回字符对应的整数
pow()幂运算
print()打印输出，默认使用空格分割、换行结尾，输出到控制台
property()属性访问的包装类
range()从0开始到stop-1的可迭代对象
repr()对象转化为供解释器读取的形式
reversed()返回一个翻转元素的迭代器
round()四舍六入五就近取偶
set()创建个set
setattr()用于设置属性值
slice()实现切片对象，主要用在切片操作函数里的参数传递。
sorted()排序
staticmethod()返回函数的静态方法。
str()字符串转换
sum()对可迭代对象的所有数值元素求和
super()用于调用父类(超类)的一个方法
tuple()将列表转换为元组
type()返回对象的类型
vars()返回对象object的属性和属性值的字典对象。
zip()将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
__import__()用于动态加载类和函数
}

  