1.#选择排序法升序
num = [3,5,1,7,9,6,8]
length = len(num)

for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if num[maxindex] > num[j]:
            maxindex = j

    if maxindex != i:
            num[i],num[maxindex] = num[maxindex],num[i]

print(num)

2.#选择排序法降序
num = [3,5,1,7,9,6,8]
length = len(num)

for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if num[maxindex] < num[j]:
            maxindex = j

    if maxindex != i:
            num[i],num[maxindex] = num[maxindex],num[i]

print(num)

3.#交换法降序
num = [3,5,1,7,9,6,8]
length = len(num)

for i in range(length):
    for j in range(length-i-1):
        if num[j] < num[j+1]:
            #tmp = num[j]
            #num[j] = num[j+1]
            #num[j+1] = tmp
            num[j],num[j+1] = num[j+1],num[j]
print(num)

4.#交换法升序
num = [3,5,1,7,9,6,8]
length = len(num)

for i in range(length):
    for j in range(length-i-1):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]
            #tmp = num[j]
            #num[j] = num[j+1]
            #num[j+1] = tmp
            
print(num)

5.#sort法升序
num = [3,5,1,7,9,6,8]
num.sort()
print(num)

6.#sort法降序
num = [3,5,1,7,9,6,8]
num.sort(reverse=True)
print(num)
