# -*- coding: utf-8 -*-
# @Time  : 2019/4/18 17:59
# @Author : xm11211
# @FileName: selection sort.py
# @Software: PyCharm
lst = [3, 5, 1, 7, 9, 6, 8]
length = len(lst)
for i in range(length // 2):
    maxIndex = i
    minIndex = -i - 1
    minOrigin = minIndex
    for j in range(i + 1, length):
        if lst[maxIndex] < lst[j]:
            maxIndex = j
        if lst[minIndex] > lst[-j - 1]:
            minIndex = -j - 1
    #假设列表是[3,2,2,2,2,1]1和3固定下来之后，最大值和最小值都等于2，说明排序已完成
    if lst[maxIndex] == lst[minIndex]:
        break
    if maxIndex != i:
        lst[maxIndex],lst[i] = lst[i],lst[maxIndex]
        #如果最小值位置上的数字正好被最大值给替换了
        #假设列表是[1,9,3,2]
        ##max=1(9) min=0/-4(1) => max=0/-4(9) min=1(1) 原1的位置替换为最小值1，原0/-4的位置替换为9
        ##需要更正最小值位置
        if minIndex == i - length:
            minIndex = maxIndex - length
    #假设列表是[1,1,1,2],当前首位1和末位2是需要进行最大值替换的，然后末位2和倒数第2位1是需要最小值替换的
    #经过一轮最大值替换。列表变为[2,1,1,1],此时末位与倒数第二位的值是相同的,都为1，没有必要做最小值替换，所以此处可做优化
    if minIndex != -i - 1 and lst[minOrigin] != lst[minIndex]:
        lst[-i - 1],lst[minIndex] = lst[minIndex],lst[-i - 1]
print(lst)