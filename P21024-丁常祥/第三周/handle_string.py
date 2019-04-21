#!/bin/env python
#
import re
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''
result = {'POST':0,'GET':0}

#第一种方法，分行，每一行中"后的一个位置开始，/前一个位置结束进行切片
log_list = logs.splitlines()

#遍历每行数据组成的数组，分行处理
for i in range(1,len(log_list)):
	per_row_str = log_list[i]
	s = (per_row_str[per_row_str.find('"')+1:per_row_str.find('/')-1]).upper()
	if s == 'POST':
		result['POST'] += 1
	if s == 'GET':
		result['GET'] += 1

print('GET请求次数为：' + str(result['GET']) + '次')
print('POST请求次数为：' + str(result['POST']) + '次')

#将上面的结果清空,顺便复习一下字典的初始化方法
result = dict(GET=0,POST=0)

#第二种方法要借助re模块,每一行中"位置+1开始，到第二个空格结束进行切片
for i in range(1,len(log_list)):
	per_row_str = log_list[i]
	second_space = [i.start() for i in re.finditer(' ',per_row_str)][1]
	start_position = per_row_str.find('"') + 1
	s = (per_row_str[start_position:second_space]).upper()
	if s == 'POST':
		result['POST'] += 1
	if s == 'GET':
		result['GET'] +=1

print('GET请求次数为：' + str(result['GET']) + '次')
print('POST请求次数为：' + str(result['POST']) + '次')
