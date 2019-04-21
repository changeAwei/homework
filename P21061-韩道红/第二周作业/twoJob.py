# 1. 简要说明Python垃圾回收机制
"""
    python中的垃圾回收是以引用计数为主，
    在Python中，如果一个对象的引用数为0，
    Python虚拟机就会回收这个对象的内存。
"""
# 2. 什么是斐波那契数列、质数、合数和猴子吃桃问题（文字说明即可）？
"""
    1斐波那契数列：从第3项开始，每一项都等于前两项之和。
    2质数：只有1本身两约数(也叫因数)的数叫质数（也叫素数）。
    3合数：除了1和他本身两个约数(也叫因数)的数叫合数。
    4猴子吃桃：是个递归思想的问题，定义一个递归函数，当递归函数中为1时递归函数返回桃子总数 
"""
# 3. 请写出列表支持的所有方法及说明（例如: append 向列表末尾添加元素）
"""
·Python中list支持以下几种操作：
    1 append 向列表末尾添加元素
    2 insert 插入一个元素 参数一：index位置 参数二：object
    3 extend(tableList) 方式三：扩展列表，参数：iterable参数
    4 L = [1,2,3], l = L[index] 索引取值 超出索引范围会报错
    5 L = [1,2,3,1,2,3] l = [:1] 切片取值(列表截取)和str类似
    6 remove 参数指定删除元素 如有重复元素，只会删除最靠前的
    7 pop pop可选参数index删除指定位置的元素 默认为最后一个元素
    8 del 可以删除整个列表或指定元素或者列表切片，list删除后无法访问
    9 clear 清除所有元素，剩下空列表
    10 reverse 反转列表中的元素
    11 sort 对列表进行排序，排序会修改list本身,不会返回新list
    12 sorted 对可迭代的序列排序生成新的序列,reverse参数接受False或者True表示是否逆序默认为False
    13 copy 返回复制后的新列表
    14 count 参数指定元素，用于统计某个元素在列表中出现的次数
    15 len 统计列表的元素个数 
"""

# 4. 实现一个简易的计算器，效果如下：
#     （1）. 运行后提示让用户输入一个数字
#     （2）. 提示输入操作符（+ - * /）
#     （3）. 再次提示输入一个数字
#     （4）. 打印计算结果
#     （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
while True:
    try:
        oneNum = int(input("请输入一个数字："))
        operator = input("请输入(+ - * /)：")
        twoNum = int(input("请输入第二个数字："))
        if operator =="+":
            print(oneNum+twoNum)

        if operator =="-":
            print(oneNum-twoNum)

        if operator =="*":
            print(oneNum*twoNum)

        if operator =="/":
            print(oneNum/twoNum)
    except:
        print('输入有误')
        pass
    quit = input("Y(y)继续|其它退出").upper()
    if quit == 'Y':
        continue
    else:
        break