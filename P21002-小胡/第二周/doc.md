### 简要说明Python垃圾回收机制
Python垃圾回收主要以引用计数为主。python使用引用计数记录所有对象的引用数，
当对象引用数变为0，它就可以被垃圾回收GC。
> #### 当发生以下四种情况的时候，该对象的引用计数器+1
+ 对象被创建  a=14
+ 对象被引用  b=a
+ 对象被作为参数,传到函数中   func(a)
+ 对象作为一个元素，存储在容器中   s1={a,b,1,2,'a','b'}
> #### 当发生以下四种情况时，该对象的引用计数器-1
+ 当该对象的别名被显式销毁时  del a
+ 当该对象的引别名被赋予新的对象   a=2
+ 一个对象离开它的作用域，例如 func函数执行完毕时，函数里面的局部变量的引用计数器就会-1（但是全局变量不会）
+ 将该元素从容器中删除时，或者容器被销毁时

#### ```当指向该对象的内存的引用计数器为0的时候，该内存将会被Python虚拟机销毁```

### 什么是斐波那契数列、素数、质数和猴子吃桃问题（文字说明即可）？
1.斐波那契数列（Fibonacci sequence），又称黄金分割数列.这个数列从第3项开始，每一项都等于前两项之和。
       
    表达式 F[n]=F[n-1]+F[n-2](n>=3,F[1]=1,F[2]=1)

2.素数又称质数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数，否则称为合数。

3.猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃
  了一个。以后每天早上都吃了前一天剩下的一半零一个。
 
 ### 列表支持的所有方法及说明
+ append(object) 列表尾部追加元素，返回None，就地修改，时间复杂度是O(1)
+ insert(index, object) 在指定的索引index处插入元素object，返回None，就地修改，时间复杂度是O(n)
+ extend(iteratable) 将可迭代对象的元素追加进来，返回None，就地修改
+ remove(value) 从左至右查找第一个匹配value的值，移除该元素，返回None，就地修改，时间复杂度为O(n)
+ pop([index]) 不指定索引index，就从列表尾部弹出一个元素  时间复杂度为O(1)；指定索引index，就从索引处弹出一个元素，索引超界抛出IndexError错误，时间复杂度为O(n)
+ clear() 清除列表所有元素，剩下一个空列表，返回None，就地修改
+ reverse() 将列表元素反转，返回None，就地修改
+ sort(key=None, reverse=False) 对列表元素进行排序，就地修改，默认升序；reverse为True，反转，降序；key一个函数，指定key如何排序，例如str
+ copy() 浅拷贝列表
+ count(value) 返回列表中匹配value的次数，时间复杂度是O(n)
+ index(value,[start,[stop]])  通过值value，从指定区间查找列表内的元素是否匹配，匹配第一个就立即返回索引，匹配不到，抛出异常ValueError，时间复杂度是O(n)
