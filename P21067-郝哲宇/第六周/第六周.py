"""
1. 什么是高阶函数和柯理化并举例说明
2. 请列出functools包内的每个函数的功能作用
3. 请使用已学习的装饰器相关知识自己实现functools.lur_cache
4. 什么是类型注解并说明其背后的目的

"""

#1. 什么是高阶函数和柯理化并举例说明。
"""
高阶函数：
    使用函数作为输入输出的函数（参数接受一个或多个函数）
柯理化：
    使用嵌套解构，外层返回的是内层函数的调用
一些内建的高阶函数：
    filter（function，iterabel） ---> 迭代器，惰性求值
        filter(lambda x:x%2==0,range(10)) 
    map(function,iterable)映射函数 ---> 返回一个迭代器，惰性求值
        map(lambda x:x+1,range(5))
        map(lambda x,y:x+y,'abc','qwe')
    ...
栗子：
def add(x,y):
    return x+y
def add1(x):
    def _add(y):
        return x+y
    return _add
ad = add
ad1 = add1
print(ad(1,2))
print(ad1(1)(2))
"""
#2. 请列出functools包内的每个函数的功能作用。
"""
from functools import partial,reduce,total_ordering,wraps
functools.cmp_to_key,将python2中的比较函数comparison function函数转换成关键字函数，接受俩个参数，比较这两个参数并根据他们的大小关系返回负值、零或者正值中的一个。关键字函数也是可调用的，接受一个参数，同时返回一个可以用作排序关键字的值：    
    def add(x,y):
        return x+y
    int1 = [2,3,1]
    print sorted(int1,key=cmp_to_key(add))

functools.partial(func,*args,**kwargs) 函数装饰器，返回一个新的partial对象。当一个函数可以接收很多参数，而某一次使用只需要修改其中一部分参数，其他参保持不变时，partial对象就可以将这些不变的对象冻结起来，然后调用需要修改的参数，然后返回一个行的partial函数
    def add(*args):
        return sum(args)
    ad1 = partial(add,100)
    print(ad1(1,2))
    
functools.reduce(function, sequence[, initial])-> value,与python内置的reduce函数功能一样
      对sequence连续使用function, 如果不给出initial, 则第一次调用传递sequence的两个元素, 以后把前一次调用的结果和sequence的下一个元素传递给function. 如果给出initial, 则第一次传递initial和sequence的第一个元素给function.
    reduce(add,(1,2,3,4,8))

functools.total_ordering 定义了多个比较排序方法，这个类装饰器将会补充其余的比较方法，被修饰的类至少有__lt__(),__le__(),__gt__()或__ge__()其中一个，同时被修饰的类应该还提供__eq__()方法

functools.wraps 这个函数可以作为一个装饰器，简化调用update_wrapper的过程，用于修改默认函数的帮助文档

    def my_decorator(f):
        # @wraps(f)
        def wrapper(*args,**kwargs):
            """Docs1"""
            print('信息1')
            return f(*args,**kwargs)
        return wrapper
    @my_decorator
    def example():
        """ Docs"""
        print('信息2')
    
    example()
    print(example.__name__)
    print(example.__doc__)
"""
#3. 请使用已学习的装饰器相关知识自己实现functools.lur_cache
"""
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    print('calling the fib function....')
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

"""

#4. 什么是类型注解并说明其背后的目的
"""
对函数的参数进行注解
对函数的返回值进行类型注解
支队函数参数做一个辅助的说明，并不对函数参数进行类型检查
提供第三方工具，做代码分析，发现隐藏的bug
函数注解的信息，保存在__annotations__
调用类方法：     函数.__annotations__
变量注解，在3.6后引入：      i: int = 3
"""
