l = [3, 5, 1, 7, 9, 6, 8]
length = len(l)
for i in range(length//2):
    maxindex = i
    minindex = -i-1
    for j in range(i+1,length):
        if l[j] > l[maxindex]:#最大值索引
            maxindex = j
        if l[-j-1] < l[minindex]:#最小值索引
            minindex = -j-1
    if maxindex != i:#正索引处理，修正索引
        l[i], l[maxindex] = l[maxindex], l[i]
        if i == minindex or minindex == i - length:
            minindex = maxindex -length
    if minindex != -i-1:#负索引处理
        l[-i-1], l[minindex] = l[minindex], l[-i-1]
print(l)