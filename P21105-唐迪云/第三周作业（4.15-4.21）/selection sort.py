log_list = [3, 5, 1, 7, 9, 6, 8]
length = len(log_list)
for i in range(len(log_list)-1):
    min = i
    for j in range(i+1,len(log_list)):
        if log_list[min] > log_list[j]:
            min = j
    temp = log_list[min]
    log_list[min] = log_list[i]
    log_list[i] = temp
print(log_list)