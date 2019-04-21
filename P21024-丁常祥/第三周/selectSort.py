#!/bin/env python
#
import random
#选择排序其实就是每次排序找出最大的值或者最小的值，一轮结束之后，再对相应位置进行交换
lst = []

for _ in range(10):
	lst.append(random.randint(0,9))

for i in range(len(lst)):#确认趟数
	max_index = i #降序排序
	for k in range(i,len(lst)):#在每一趟中找出最大的索引
		if lst[k] > lst[max_index]:
			max_index = k
	if max_index != i:
		tmp = lst[i]
		lst[i] = lst[max_index]
		lst[max_index] = tmp
print(lst)
