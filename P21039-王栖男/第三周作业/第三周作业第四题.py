#4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
lst = [3, 5, 1, 7, 9, 6, 8]
length = len(lst)

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

