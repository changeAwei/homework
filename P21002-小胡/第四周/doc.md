### 什么是杨辉三角和转置矩阵
1.杨辉三角以正整数构成，数字左右对称，每行由1开始逐渐变大，然后变小，回到1。除每行最左侧与最右侧的数字以外，每个数字等于它的左上方与右上方两个数字之和（也就是说，第n行第k个数字等于第n-1行的第k-1个数字与第k个数字的和）

2.将矩阵的行列互换得到的新矩阵称为转置矩阵，转置矩阵的行列式不变。
### 说明列表和Set集合的相同点和不同点。
> ####相同点
+ 都可以迭代
+ 都是可变的
> ####不同点
+ 集合是无序的、不重复、非线性的数据结构，元素必须可hash且不可索引
+ 列表是有序的、可重复、线性的数据结构，元素可以是任意对象且可索引
### Set集合支持的所有方法及说明
+ add(elem) 增加一个元素到set中，如果元素存在，什么都不做，set和list无法作为add参数直接加入
+ update(*others) 合并其他元素到set集合中来，参数others必须是可迭代对象，就地修改
+ remove(elem) 从set中移除一个元素，元素不存在，抛出KeyError异常
+ discard(elem)  从set中移除一个元素，元素不存在，什么都不做
+ pop() 移除并返回任意的元素,空集返回KeyError异常
+ clear() 移除所有元素
### 字典支持的所有方法及说明
+ dict(**kwargs)使用name=value对初始化一个字典
+ dict(iterable, **kwarg) 使用可迭代对象和name=value对构造字典，不过可迭代对象的元素必须是一个二元结构
+ dict(mapping, **kwarg) 使用一个字典构建另一个字典
+ fromkeys(iterable, value) 使用可迭代对象构造字典
+ d[key] 返回key对应的值value,key不存在抛出KeyError异常
+ get(key[, default]) 返回key对应的值value, key不存在返回缺省值，如果没有设置缺省值就返回None
+ setdefault(key[, default]) 返回key对应的值value,key不存在，添加kv对，value设置为default，并返回default，如果default没有设置，缺省为None
+ d[key] = value 将key对应的值修改为value,key不存在添加新的kv对
+ update([other])  使用另一个字典的kv对更新本字典, key不存在，就添加,key存在，覆盖已经存在的key对应的值,就地修改
+ pop(key[, default]), key存在，移除它，并返回它的value,key不存在，返回给定的default,default未设置，key不存在则抛出KeyError异常
+ popitem() 移除并返回一个任意的键值对,字典为empty，抛出KeyError异常
+ clear()  清空字典
### Python内建函数及说明
+ id 返回对象的唯一标识，CPython返回内存地址
+ hash() 返回一个对象的哈希值
+ type() 返回对象的类型
+ 类型转换 float() int() bin() hex() oct() bool() list() tuple() dict() set() complex()  bytes() bytearray()
+ input([prompt]) 接收用户输入，返回一个字符串
+ print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) 打印输出，默认使用空格分割、换行结尾，输出到控制台
+ 对象长度len(s) 返回一个集合类型的元素个数
+ isinstance(obj, class_or_tuple) 判断对象obj是否属于某种类型或者元组中列出的某个类型
+ issubclass(cls, class_or_tuple) 判断类型cls是否是某种类型的子类或元组中列出的某个类型的子类
+ abs(x) 绝对值 
+ max()最大值 min()最小值 返回可迭代对象中最大或最小值,返回多个参数中最大或最小值
+ round(x) 四舍六入五取偶
+ pow(x , y) x的y次方
+ range(stop) 从0开始到stop-1的可迭代对象；range(start, stop[, step])从start开始到stop-1结束步长为step的可迭代对象
+ divmod(x, y) 等价于tuple (x//y, x%y)
+ sum(iterable[, start]) 对可迭代对象的所有数值元素求和
+ chr(i) 给一个一定范围的整数返回对应的字符
+ ord(c) 返回字符对应的整数
+ sorted(iterable[, key][, reverse]) 排序，返回一个新的列表，默认升序
+ reversed(seq) 返回一个翻转元素的迭代器
+ enumerate(seq, start=0) 枚举，迭代一个序列，返回索引数字和元素构成的二元组
+ iter(iterable) 将一个可迭代对象封装成一个迭代器
+ next(iterator[, default]) t对一个迭代器取下一个元素。如果全部元素都取过了，再次next会抛StopIteration异常
+ zip(*iterables) 把多个可迭代对象合并在一起，返回一个迭代器
