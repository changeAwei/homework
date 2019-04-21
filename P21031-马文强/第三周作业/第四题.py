num = [3,5,1,7,9,6,8]
length = len(num)
for i in range(length):
    maxindex = i
    for j in range(i+1, length):
        if num[maxindex] < num[j]:
            maxindex = j
    if i != maxindex:
        num[maxindex],num[i] = num[i],num[maxindex]
print(num)