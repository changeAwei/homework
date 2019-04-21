#!/usr/bin/python

"""

1. 说明列表的浅拷贝和深拷贝的区别
2. 说明列表和元组的相同点和不同点
3. 请写出字符串支持的所有方法及说明（例如: lower 返回字符串的小写）
4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
POST 2
GET 3
下边是logs变量：
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' 
"""

#深拷贝和浅拷贝的区别
import copy
'''

返回值是：
[1, 2, 3, 4, ['11', '22']]
29100152 58484496 58485256
-------------------
[1, 2, 3, 4, [2, '22']] ---- [1, 2, 3, 4, [2, '22']]
[1, 2, 3, 4, ['11', 22]] ---- [1, 2, 3, 4, [2, '22']]
29100152 58484496 58485256

在我看来浅拷贝像一个快捷方式实际操作的还是这个链接的对象本身
而深拷贝像是复制的镜像，在新开辟的空间中操作
'''

lst = [1,2,3,4,['11','22']]

lst1=lst.copy()

lst2=copy.deepcopy(lst)
print(lst2)

print(id(lst),id(lst1),id(lst2))
print('-------------------')

lst1[4][0]=2
print(lst1,'----',lst)

lst2[4][1]=22
print(lst2,'----',lst)

print(id(lst),id(lst1),id(lst2))

#列表和元组的相同点和不同点
"""

相同点:
    都可以通过index取值（序列类型容器），可以存放任何类型数据、支持切片、迭代等操作

不同点:
    tuple()元素不可变，元组里的元素没有字段命名属性（没有字段名）。列表[]是可变类型、数据可以动态变化
"""

#请写出字符串支持的所有方法及说明（例如: lower 返回字符串的小写）
"""

字符串相加：a='hello' b='word' print(a+b) --> 世界你好
字符串乘：a='超级英雄' print(a*2) ---> 超级英雄超级英雄
字符串索引：a='abcd' print(a[1]) ---->a
字符串切片：a='xiaohong' print(a[0:4]) --->xiao  #可以设置补长
字符大写：a=‘xiaohong’ a.upper()
字符小写：a='XIAOHONG' a.lower()
首字符大写： a='xiaohong' a.capitalize()
大小写转换：a='xiaohong' a.swapcase()
判断这个字符串的开头：a='xiaohong' a.startswith('x') -->返回bool值
判断这个字符串的结尾：a='xiaohong' a.endswith('g') -->返回bool值
统计字符串当中相同元素的个数：a='aabbbcccc' a.count('a') -->返回int类型
获取字符串的index：a='xiaohong' a.find('g') 
字符串转换成其他格式：a.encode()
字符串的判断：a.islower/a.isupper()/a.isstartswith/a.isendswith...
"""

#使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
"""

这里使用升序和降序
lst=[3,5,1,7,9,6,8]
#降序：
lst=[3,5,1,7,9,6,8]
length = len(lst)
print(length)

count = 0
for i in lst:
    count+=1
length1=count
print(length1)

lst1=[]
for _ in range(length1):
    c = 0
    for i in lst:
        if i > c:
            c = i
    lst.remove(c)
    lst1.append(c)
print(lst1)

#升序：
for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if lst[maxindex] < lst[j]:
            maxindex = j

    if i != maxindex:
        temp =lst[i]
        lst[i] = lst[maxindex]
        lst[maxindex] = temp

print(lst)

"""

#有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
"""

POST 2
GET 3
下边是logs变量：
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' 

"""

logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
#第一种
log_lst = logs.split(" ")

lst1 = log_lst[1:-1:5]
lst1_keywords=" ".join(lst1)
lst1_upper=lst1_keywords.upper()
print('POST',lst1_upper.count('POST'))
print('GET',lst1_upper.count('GET'))

#优化
log_lst = logs.strip().splitlines() #转化成去重空格并去除换行符的列表
list_meth=[]
for i in log_lst:
    list_meth.append(i.split()[1].replace('"','').upper()) #提取第二个关键字并替换引号
print(list_meth)
log_dic={}
for i in list_meth:
    log_dic[i] = log_dic.get(i,0)+1
print(log_dic)
