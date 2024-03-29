###########################
# 1.计算器
while True:
    num1 = input('请输入第一个数，退出请输入quit>>>')
    if num1 == 'quit':
        break
    num1 = int(num1)
    operator = input('请选择运算方式+、-、*、/，退出请输入quit>>>')
    if operator == 'quit':
        break
    num2 = input('请输入第二个数，退出请输入quit>>>')
    if num2 == 'quit':
        break
    num2 = int(num2)
    if operator == '+':
        print(num1,'+',num2,'=',num1+num2)
    elif operator == '-':
        print(num1,'-',num2,'=',num1-num2)
    elif operator == '*':
        print(num1,'*',num2,'=',num1*num2)
    elif operator == '/':
        print(num1,'/',num2,'=',num1/num2)
    else:
        print("输入错误,请重新输入！，退出请输入quit")


##########################
# 2.Python 垃圾回收机制
# python中每一个东西都是对象，每当一个对象被引用后内部会有一个引用计数
# 如果引用计数为0时，该对象生命就结束了，内存将被释放掉。
# 引用计数机制的优点：
# 1.简单
# 2.实时性
# 缺点：
# 维护引用计数消耗资源
# 循环引用易造成内存泄漏

##########################
# 3.1 斐波拉契数列
# 前两项相加第三项之和
# 3.2 质数和素数
# 一个大于1的整数，且只能整除他自身和1的正整数
# 3.3 猴子吃桃
# 若干个桃子，第一天吃了一半加一个，第二天又将剩下的桃子吃了一半加一个...以此类推
# 可以使用递归的方法来实现

##########################
# 4.list列表支持的所有方法及说明
# -1.append:向后追加一个元素
# -2.extand:在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# -3.insert:某处插入一个元素，后面的元素都将向后挪动
# -4.pop:默认从尾部弹出一个元素，返回这个元素
# -5.remove:移除一个元素，后面的元素向前挪动
# -6.count:列表元素计数
# -7.index:索引某一个元素
# -8.sort:对原列表进行排序
