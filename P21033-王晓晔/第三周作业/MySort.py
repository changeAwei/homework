list1 = [3, 5, 1, 7, 9, 6, 8]

length = len(list1)
for i in range(length):
    temp = list1[i]
    k = i
    for j in range(i + 1, length):
        if list1[j] < temp:
            temp = list1[j]
            k = j
    list1[k] = list1[i]
    list1[i] = temp

print(list1)