def SelectionSort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] < l [i] :
                l[i] , l[j] = l[j], l[i]
    return l



list = [3, 5, 1, 7, 9, 6, 8]
new_list = SelectionSort(list)
print(new_list)
