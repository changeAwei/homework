#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2019/4/18 21:25
# @Author : Fly
# @FileName: 第三周作业.py
# @Software: PyCharm

# 冒泡排序  非封装解构
lst = [3,5,1,7,9,6,8]
length = len(lst)
for i in range(length-1):  # h行数
    for j in range(length-i-1):  # 比较次数
        if lst[j] > lst[j+1]:
            tmpmax = lst[j]
            lst[j] = lst [j+1]
            lst[j+1] = tmpmax
print(lst)

# 冒泡排序  封装解构
lst = [3,5,1,7,9,6,8]
length = len(lst)
for i in range(length):
    for j in range(length-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)

# 选择排序  优化点：利用正负索引，每一行进行两次比较。
lst = [3,5,1,7,9,6,8]
length = len(lst)
for i in range(length):
    tmpmin = i
    for j in range(i+1,length):
        if lst[tmpmin] > lst [j]:
            tmpmin = j
    if i != j :
        lst[i],lst[tmpmin] = lst[tmpmin],lst[i]
print(lst)

# log变量
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
tmplst =  logs.replace('"',' ').upper().split()
tmppost = tmplst.count('POST')
tmpget = tmplst.count('GET')
print('POST:{}'.format(tmppost))
print('GET:{}'.format(tmpget))