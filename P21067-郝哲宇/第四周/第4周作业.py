"""
1. 什么是杨辉三角和转置矩阵（文字说明即可）？
　杨辉三角的本质特征是：
        他的俩条斜边有事由数值1组成，二其余的数则是等于他肩上的俩个数之和：
            如果用二项式表示其推导式：
            (a+b)^n
                n=0 (a+b)^0  1 = 1
                n=1 (a+b)^1   1 1  = 2
                n=2 (a+b)^2 = a^2+2ab+b^2  1 2 1  = 4
                n=3 (a+b)^3 = a^3+3a^2b+3ab^2+b^3  1 3 3 1  =8
                n=4 (a+b)^4 = a^4+4a^3b+6a^2b^2+4ab^3+b^4  1 4 6 4 1  =16

    转置矩形：
        将矩阵的行列互换得到的新矩阵称为转置矩阵，转置矩阵的行列式不变。
            例如：
                m=[[1,2],[3,4],[5,6][7,8]]  transfrom=[[1,3,5,7],[2,4,6,8]]

2. 说明列表和Set集合的相同点和不同点。
　       相同点：
         它们都是容器，里边放置成员
         不同点：
         set的成员可以hash，list的成员不可hash
         list的成员有索引，set的成员是无序的

3. 请写出Set集合支持的所有方法及说明（例如：add 向Set集合中添加一个元素）
    s={"刘嘉玲","王祖贤","张曼玉"}
    set的方法：
        增加：
            s.add("关之琳")
            s.update(['王佳乐','田淑芬','郝英俊'])
        删除：
            s.pop() #随机跳出来一个
            s.remove("王祖贤") #直接删除元素，没有会报错__KeyError
            s.clear()   #格式化这个set
        修改： #应为集合中没有索引无法定义一个元素，修改只能是删除添加
            s.remove("张曼玉") s.add("东方不败")
        查询：
            可以通过迭代的方式获取 for i in s: print(i)
    set的运算：
    s1 = {"刘嘉玲", "王祖贤", "张曼玉"}
    s2 = {"姚贝娜","刘嘉玲"}
        交集：print(s1&s2) print(s1.intersection(s2))
        并集：print(s1|s2) print(s1.union(s2))
        差集：print(s1-s2) print(s1.difference(s2))
        反交集：print(s1 ^ s2) print(symmetric_difference(s2))
        子集：print(s1<s2) print(s1.issubset(s2))
        父集：print(s1>s2) print(s1.issuperset(s2))

4. 请写出字典支持的所有方法及说明（例如：pop 从字典中移除指定的key并返回其value）
    字典(dict)是python中唯⼀的⼀个映射类型.他是以{ }括起来的键值对组成. 在dict中key是唯⼀的.在保存的时候, 根据key来计算出⼀个内存地址. 然后将key-value保存在这个地址中.
    已知的可哈希(不可变)的数据类型: int, str, tuple, bool
    不可哈希(可变)的数据类型: list, dict, set
    dict的方法：
    dic={}
        增加：
            dic['name']='张美玲'
            dic['age']=18
            dic.setdefault('王菲','歌手') #设置默认元素
        删除：
            print(dic.pop("王菲")) #删除对于的元素，并返回元素的值
            print(dic.popitem()) #删除一个元素，范返回这个元素的k,v. 3.6默认删除最后一个（建议用第一种）
            dic.clear() #格式化字典
        改：
            dic['王菲']='我女神' #给k重新赋值
            dic.update({'age':18,'sex':'woman'}) #添加新的内容到字典中，有的话就覆盖
        查：
            print(dic['王菲']) #有k就返回，没有就报KeyError
            dic.get("王菲") #有没有k都返回，不存在的k返回None

        获取字典的健：
            dic.keys()
        获取字典的值：
            dic.values()
        获取字典的键值对：
            dic.items()
5. 请写出内建函数及说明（参考：https://docs.python.org/3/library/functions.html）
        abs() 取绝对值
        delattr()与setattr()	删除一个对象的属性或方法和setattr() 相反
        hash() 获取一个对象的hash值
        memoryview() 返回给定参数的内存查看对象
        set() 创建集合的的函数
        all()与any() 判断一个可迭代对象，返回一个bool值any表示任意，all表示所有
        dict() 创建字典的函数
        help()	帮组函数
        min()与max() 获取最小值 ，获取最大值
        dir() 查看对象描述
        hex() 进制转换（默认16进制）
        next()	获取一个可迭代对象的下一个值（如获取生成器中yield值）
        slice() 切片
        ascii()	查看ascii编码
        divmod() 取模
        id() 查看内存地址
        object() 默认的基类
        sorted() 排序
        bin() 将一个整数转换成二进制
        enumerate()	枚举一个可迭代对象
        input()	获取交互输入
        oct()	转化成8进制
        staticmethod() 在类中将一个方法转发成静态属性
        bool() 判断一个对象的bool类型
        eval() 执行一个字符串表达式,并返回表达式的值
        int() 转化int类型
        open() 打开一个文件默认‘r’
        str() 转化str类型
        breakpoint() 调试器3.7的新功能，没用过
        exec() 执行代码
        isinstance() 判断一个对象的类型
        ord() 与chr() unicode编码
        sum() 返回可迭代对象的累计求和值
        bytearray() 字节数组（二进制，encode,decode）
        filter() 过滤函数
        issubclass() 判读是否是class的子类返回true
        pow() 幂运算
        super()  引用父类的属性
        bytes() 返回字节码
        float() 返回浮点数
        iter() 返回一个迭代器对象 通过for I in iter(obj): 取值
        print() 打印一个对象
        tuple() 生成一个元组
        callable() 判断参数是否可以调用
        format() 格式化函数
        len() 获取obj长度，实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）
        property() 获取class的方法
        type() 获取对象类型
        frozenset() 将一个新的可迭代对象变成一个不可变集合（tuple类型）
        list() 创建一个列表
        range() 返回一个不可变序列（tuple类型）
        vars() 返回对象的描述信息__dict___
        classmethod() 类方法
        getattr() 获取class中传入的参数
        locals()与globals() 本地 ，全局
        repr() 转化为供解释器读取的形式
        zip() 创建一个聚合了来自每个可迭代对象中的元素的迭代器。
        compile() 将一个字符串编译为字节代码
        map() 返回一个迭代器，将一个function和迭代器作为参数
        reversed() 翻转
        __import__() 没用过
        complex() 返回一个复数
        hasattr() 判断这个类中是否有这个方法或属性
        round() 四舍五入
"""



































