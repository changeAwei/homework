# 1.什么是高阶函数和柯理化并举例说明。

#高阶函数
#可以接受传入函数作为参数，或者输出一个函数的是高阶函数
def a(x, y, fn):
    return fn(x, y)
print(a(6, 3, lambda x, y:x - y))

#柯里化
#将原本接收参数的函数变成新的接收一个参数的过程，新的函数返回一个以原有第二个参数为参数的函数
def add(x):
    def _add(y):
        return x + y
    return _add
print(add(5)(6))

# ------------------------------------------------------------------------------------------------------------------
# 2.请列出functools包内的每个函数的功能作用
'''
functools.partial(func, *args, **keywords)
把函数的部分参数固定下来，相当于为部分的参数添加了一个固定的默认值，返回一个新函数

functools.update_wrapper(wrapper, wrapped[, assigned][, updated])
通过partial生成的函数通常会缺失name，doc等属性，可用update_wrapper进行更新

functools.partialmethod(func, *args, **keywords)
类方法，可用来将一个函数变成类方法

functools.total_ordering(cls)
这是一个类装饰器，给定一个类，这个类定义了一个或多个比较排序方法，这个类装饰器将会补充其余的比较方法，减少了自己定义所有比较方法时的工作量。

functools.cmp_to_key(func)
将老版本的比较函数转化为关键字函数，例如 sorted(iter, key=cmp_to_key(locale.strcoll))

functools.lru_cache(maxsize=128, typed=False)
缓存装饰器，可以让函数调用的参数保存在缓存中，如果再次调用同样的参数，则不用再次执行函数，可以直接获得结果

functools.reduce(function, iterable[, initializer])
用function从左至右依次计算iterable序列中的项。
例如reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])会计算((((1+2)+3)+4)+5)。左边的参数x是计算出的值，右边的参数y是从序列中更新的值

functools.singledispatch(default)
有时函数传入参类型不同， 函数处理逻辑可能也不同， singlepatch提供了这样一种机制，可以在默认函数实现的基础上注册其他不同类型传入参数的函数逻辑实现。
'''

# ------------------------------------------------------------------------------------------------------------------
# 3.请使用已学习的装饰器相关知识自己实现functools.lur_cache。

import collections
import time

def lur_cache(fn):
    local_cache = {}
    def wrapper(*args, **kwargs):
        dic = collections.OrderedDict()
        for i,v in enumerate(args):
            dic[i] = v
        dic.update(kwargs)
        key = tuple(dic.items())
        if key not in local_cache:
            local_cache[key] = fn(*args, **kwargs)
        return local_cache[key]
    return wrapper

@lur_cache
def add(x, y):
    # time.sleep(2)
    return x + y
print(add(4, y=6))

# ------------------------------------------------------------------------------------------------------------------
# 4.什么是类型注解并说明其背后的目的。

# python中的函数不管是形参的定义还是函数的返回值，都没有规定类型，
# 为了避免传入错误的类型或接收错误的返回值导致函数调用过程中抛出异常，需要使用类型注解来注明参数、返回值的类型
# 类型注解只是做一个辅助说明，并不会检查函数参数、返回值的类型是否符合类型规定
