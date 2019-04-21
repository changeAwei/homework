lst = [3, 5, 1, 7, 9, 6, 8]
for i in range(len(lst)-1):
    index = i
    for j in range(i+1,len(lst)):
        if lst[j] > lst[index]:
            index = j
    lst[i],lst[index] = lst[index],lst[i]
print(lst)
