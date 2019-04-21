#使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
lst1 = [3, 5, 1, 7, 9, 6, 8]
for i in range(6):
    for j in range(i+1, 6):
        if lst1[i] > lst1[j]:
            a = lst1[j]
            lst1[j] = lst1[i]
            lst1[i] = a
print(lst1)
            
            
    
