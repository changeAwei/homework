#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2019/4/19 19:46
# @Author : donghui
# @FileName: homework_weed3.py
# @Software: PyCharm
#1. 说明列表的浅拷贝和深拷贝的区别c
#import copy
#浅拷贝（copy）：浅拷贝指拷贝后生成的对象（假设b）与原对象(假设a)指向同一个内存地址（假设c），此时修改a（实际修改的为内存地
# 址）时，b也会同时改变，反之也一样。例如：*号生成的、连等生成的都是浅拷贝
#深拷贝（deepcopy）：深拷贝会将拷贝对象完全拷贝一份，在内存中另外开辟一个位置，内存地址与原对象完全不同，调用deepcopy

#2. 说明列表和元组的相同点和不同点
# 相同点：
# 都是排列整齐的（可通过索引查找）、线性的、可迭代的队列
# 都可以通过索引查找对应位置的元素list[index],tuple[index]
# 都可以进行查询：   通过value查找索引:.index(value[start,[stop]])
#                   查找value在列表/元组中的次数：.count(value)
#                   len(list)，len(tuple)确认列表、元组内元素数量
# 不同点：
# 元组是不可变的，不可以进行增删改操作

#3. 请写出字符串支持的所有方法及说明（例如: lower 返回字符串的小写）
# 字符串是由一个个字符组成的有序的不可变的可迭代的序列
# 字符支持索引访问，与列表元组相同
# 字符串拼接：
# 1、符号+法：str + str 返回由两个字符串拼接起来的新字符串
# 2、jion： 'string'.jion(iterable) 将可迭代对象（可迭代对象内容需是字符串，可用迭代器生成）用
# 分隔符string一一拼接起来，返回一个新的字符串
# 字符串分割：
# 1、split:
#   str.split(string,[maxsplit = count]) 将字符串str根据分隔符string(不填则默认空格)从左往右
#   (rsplit从右往左)切开count(默认-1，从头遍历到尾，有多少切多少)次，返回各段字符串（不含分隔符）
#   组成的列表
# 2、splitlines:
#   str.splitlines(flg) 将字符串按行切开返回各段字符串（默认flg=False不含分隔符，填True则包含）组成的列表
#   使用str.splet(\n)也能达到这种效果
# 3、partition:
#   str.partition(string) 将字符串根据分隔符string(必须指定)从左往右(rpartition则从右往左)分割成三部分(string前一部分
#   string一部分,string后一部分)组成元组，如果没有找到分隔符string，则返回元组(,,str)
# 字符串排版（返回新字符串）：
# 1、改变大小写
#   str.upper() 全大写   str.lower()  全小写     str.swapcase()  大小写交换    str.title()   每个单词开头都大写(标题行)
#   str.capitalize()   首个单词开头大写(正文每段开头首字母大写)
# 2、设置字符串长度及对齐方式
#   str.center(width[,fillchar]) 按宽度width打印(若str长度大于width,也会全部打印)，后面位置用fillchar填充（默认空格）
#   str.zfill(width)            按宽度width打印(靠右)(若str长度大于width,也会全部打印)，前面使用0填充
#   str.ljust(width[,fillchar])/str.rjust(width[,fillchar])
#   按宽度width对齐（l左r右）(若str长度大于width,也会全部打印)，后面位置用fillchar填充（默认空格）
# 字符串修改（返回新字符串）
# 1、str.replace(old,new[,count])
#   将字符串中对应的old字符修改为new字符，count为修改次数(默认遍历)
# 2、str.strip(chars)
#   从字符串两端分别去除字符集chars(默认空白字符(空格\t\n\r))内所有的字符，碰到不包含在chars内的则停止
# 3、查找
#   str.find(str1[,start[,end]])  rfind   index   rindex
#   从左往右查找字符串str1在字符串str所在的索引(找到第一个就返回，前面加r从右往左)，如果没找到则返回-1
#   （index返回异常valueError）
#   str.count(str1[,start[,end]])
#   查找字符串str1在str内出现的次数，可指定索引范围
# 4、判断（返回bool值）
#   str.endswith(str1[,start[,end]])      startswith
#   字符串str是否以str1开头/结尾，可指定区间(默认遍历)
#   isalnum()      是否由字母数字组成
#   isalpha()      是否只包含字母
#   isdecimal()    是否只包含十进制数字
#   isdigit()      是否全部是数字
#   isidentifier() 是否以字母或下划线开头，其他只包含字母、数字或下划线(变量命名规则)
#   islower        是否全是小写
#   isupper        是否全是大写
#   isspace        是否只包含空白字符
# 5、格式化
#   '{}{}{key}'.format(*args,**kwargs)
#   将一个元组args中的各个元素按顺序(占位符内可填索引指向元素对应索引的元素)一一对应放入对应的占位符{}中，要求占位符一定要
#   有对应元素填入
#   将一个字典kwargs中key对应的值填入占位符内
#   占位符{}内
#       [index]可以访问对应元素索引位置
#       :<   :>     左对齐   右对齐  后面可以填数字表示宽度，数字前可以填0补充空位(默认空格)
#       :d   :x    :o   :b      将对应数字转换进制输出

#4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
def fn(nums):
    if isinstance(nums,list):
        n = nums   #不替换则原地修改
        for i in range(len(n)//2):
            maxindex = i
            minindex = -i - 1
            for j in range(i+1,len(n)-i):
                if n[j] > n[maxindex]:
                    maxindex = j
                if n[j - 1] < n[minindex]:
                    minindex = j - 1
            if i != maxindex:
                n[maxindex],n[i] = n[i],n[maxindex]
                if i == minindex:
                    minindex = maxindex
            if minindex != -i -1:  n[minindex],n[-i-1] = n[-i-1],n[minindex]
        return n
    return '无法排序'
lst = [3, 5, 1, 7, 9, 6, 8]
print(fn(lst))

#5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
#POST 2
#GET 3
#下边是logs变量：
#logs = '''
#111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
#111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
#111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
#223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
#111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
#'''

logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
a = logs.strip().splitlines()
dic = {}
for i in range(len(a)):
    var = a[i].split(maxsplit=2)
    #print(var)
    var2 = var[1].strip('\"').upper()
    if var2 in dic:
        dic[var2] += 1
    else:
        dic[var2] = 1
print(dic)