#1. 简要说明Python垃圾回收机制
    '''
    我的理理解是py的垃圾回收和引用计数有关系，每次多一次调用引用次数加1反之减1，如果引用次数等于0，则会出发py的垃圾回收，释放内存。
    '''
#2. 什么是斐波那契数列、素数、质数和猴子吃桃问题（文字说明即可）？
    '''
    斐波那契数列：
      黄金分割数列，指的是：0、1、2、3、5、8、13、21、34 。。。。。。 
      算法：Fn = F[n-1]+ F[n-2](n=>2)
    
    素数,质数：
      质数又叫素数：只能被自己或者1整除且大于1的数，有无限多个.
      条件：Fn % Fn = 1 and >= 2 
      
    猴子吃桃问题：
      无非就是饿了嘛
      最后一天剩下一个桃子，倒数第二天剩四个桃子，倒数第三天剩10桃子。。。。。。（1：1，2：4，3：10，4：22，5：46，6：94）以此类推它的成长过程哈哈
    '''
#3. 请写出列表支持的所有方法及说明（例如: append 向列表末尾添加元素）
    '''
    list列表是python的基础数据类型之一 ,其他编程语言也有类似的数据类型:
        lst = ['刘德华','周润发','周杰伦','向华强'] 
            1、按index取值：print(lst[0]) print(lst[1])
            2、安index修改：lst[0] = '皮皮红' 
            3、列表切片：lst[0:3]/lst[:3]/lst[1::2]/lst[2::-1]/lst[-1:-3:-2]
            4、列表尾部追加：lst.append（'皮皮红2号'）
            5、插入：lst.insert(2,'周杰伦2号')#整体会向后挪动一位
            6、迭代添加到列表：lst.extend('iterable')
            7、通过下标删除：lst.pop(2) #周杰伦2号干掉周杰伦，默认删除最后一项
            8、通过元素删除：lst.remove('周杰伦2号') # 如果删除的元素不存在则报错
            9、清空大法：lst.clear
            10、list翻转：lst.reverse()
            11、list排序：lst.sort(#reverse=False) #排序后重新赋值给lst并返回None
            12、list计数：lst.count('周润发') #发哥是唯一的
            13、list获取长度：len(lst) #的到元素有多少个
            14、。。。。。。
    
    '''
#4. 实现一个简易的计算器，效果如下：
#    （1）. 运行后提示让用户输入一个数字
        '''
        input('用户输入一个数字#:')
        '''
#    （2）. 提示输入操作符（+ - * /）
        '''
        input('提示输入操作符（+ - * /）#:')
        '''
#    （3）. 再次提示输入一个数字
        '''
        input('再次输入一个数字#:')
        '''
#    （4）. 打印计算结果
        '''
        print('{1}{+-*/}{2}:{运算结果}',format())
        '''
#    （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计 
'''
while True:
    one = input('用户输入一个数字#:')
    two = input('再次输入一个数字#:')
    operation = input('提示输入操作符（+ - * /）#:')
    if operation == '+':
        print('{}{}{}={}'.format(one,operation,two,int(one)+int(two)))
    if operation == '-':
        print('{}{}{}={}'.format(one, operation, two, int(one)-int(two)))
    if operation == '*':
        print('{}{}{}={}'.format(one, operation, two, int(one)*int(two)))
    if operation == '/':
        print('{}{}{}={}'.format(one, operation, two, int(one)/int(two)))
    FLAG = input('输入q 退出,输入c继续')
    if FLAG=='q' or FLAG=='Q':
        break
        if FLAG=='C' or FLAG=='c':
            continue
'''
