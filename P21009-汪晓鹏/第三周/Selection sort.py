
#使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
l = [3, 5, 1, 7, 9, 6, 8]
length = len(l)
for i in range(length):
    maxindex = i
    for j in range(i+1, length):
        if l[j] > l[maxindex]:
            maxindex = j
    if maxindex != i:
        l[maxindex], l[i] = l[i], l[maxindex]
print(l)
