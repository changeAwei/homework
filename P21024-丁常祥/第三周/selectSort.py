#!/bin/env python
#
import random
#ѡ��������ʵ����ÿ�������ҳ�����ֵ������С��ֵ��һ�ֽ���֮���ٶ���Ӧλ�ý��н���
lst = []

for _ in range(10):
	lst.append(random.randint(0,9))

for i in range(len(lst)):#ȷ������
	max_index = i #��������
	for k in range(i,len(lst)):#��ÿһ�����ҳ���������
		if lst[k] > lst[max_index]:
			max_index = k
	if max_index != i:
		tmp = lst[i]
		lst[i] = lst[max_index]
		lst[max_index] = tmp
print(lst)
