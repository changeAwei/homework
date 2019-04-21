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

#��һ�ַ��������У�ÿһ����"���һ��λ�ÿ�ʼ��/ǰһ��λ�ý���������Ƭ
log_list = logs.splitlines()

#����ÿ��������ɵ����飬���д���
for i in range(1,len(log_list)):
	per_row_str = log_list[i]
	s = (per_row_str[per_row_str.find('"')+1:per_row_str.find('/')-1]).upper()
	if s == 'POST':
		result['POST'] += 1
	if s == 'GET':
		result['GET'] += 1

print('GET�������Ϊ��' + str(result['GET']) + '��')
print('POST�������Ϊ��' + str(result['POST']) + '��')

#������Ľ�����,˳�㸴ϰһ���ֵ�ĳ�ʼ������
result = dict(GET=0,POST=0)

#�ڶ��ַ���Ҫ����reģ��,ÿһ����"λ��+1��ʼ�����ڶ����ո����������Ƭ
for i in range(1,len(log_list)):
	per_row_str = log_list[i]
	second_space = [i.start() for i in re.finditer(' ',per_row_str)][1]
	start_position = per_row_str.find('"') + 1
	s = (per_row_str[start_position:second_space]).upper()
	if s == 'POST':
		result['POST'] += 1
	if s == 'GET':
		result['GET'] +=1

print('GET�������Ϊ��' + str(result['GET']) + '��')
print('POST�������Ϊ��' + str(result['POST']) + '��')
