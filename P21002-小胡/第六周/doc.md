### 什么是高阶函数和柯理化并举例说明。
####高阶函数
 数学概念y=g(f(x))
 
 在数学和计算机科学中，高阶函数应当是至少满足下面一个条件的函数
+ 接受一个或多个函数作为参数

        filter(function, iterable)
        for x in filter(lambda x: x[0], zip(range(5),range(10))):
             print(x)
+ 输出一个函数
 
        def counter(base):
            def inc(step=1):
                base  +=  step
                return  base
            return  inc
#### 柯里化
+ 将原来接受两个参数的函数变成新的接受一个参数的函数的过程。新的函数返回一个以原有第二个参数为参数的函数
### 请列出functools包内的每个函数的功能作用。
    
        将加法函数柯里化
            def  add(x,  y):
                return  x +  y
        转换如下
            def  add(x):
                 def  _add(y):
                    return  x+y
                 return  _add
        
+ reduce(function, iterable[, initializer]) 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
+ partial(func, *args,  **keywords) 函数在执行时，要带上所有必要的参数进行调用。但是，有时参数可以在函数被调用之前提前获知。这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。偏函数是将所要承载的函数作为partial()函数的第一个参数，原函数的各个参数依次作为partial()函数后续的参数，除非使用关键字参数。
+ lru_cache 装饰器函数，将函数传入的参数组合作为键，将返回值作为值存入到字典中，达到缓存的效果
### 什么是类型注解并说明其背后的目的。 
类型注解：对函数的参数进行类型注解,对函数的返回值进行类型注解,只对函数参数做一个辅助的说明，并不对函数参数进行类型检查
目的：解决python作为动态语言定义的弊端
+ 难发现：由于不做任何类型检查，直到运行期问题才显现出来，或者线上运行时才能暴露出问题
+ 难使用：函数的使用者看到函数的时候，并不知道你的函数的设计，并不知道应该传入什么类型的数据