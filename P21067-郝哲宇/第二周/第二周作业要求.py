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
      条件：Fn = Fn % Fn  
      
    猴子吃桃问题：
    '''
#3. 请写出列表支持的所有方法及说明（例如: append 向列表末尾添加元素）
#4. 实现一个简易的计算器，效果如下：
#    （1）. 运行后提示让用户输入一个数字
#    （2）. 提示输入操作符（+ - * /）
#    （3）. 再次提示输入一个数字
#    （4）. 打印计算结果
#    （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计 
