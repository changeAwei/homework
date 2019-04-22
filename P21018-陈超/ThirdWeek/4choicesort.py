def choicesort(lst):
    sortedlst = []
    while len(lst) - 1:
        minimum = lst[0]
        index = 0
        for i in range(1,len(lst)):
            if minimum > lst[i]:
                minimum = lst[i]
                index = i
        sortedlst.append(lst.pop(index))

    sortedlst.append(lst.pop())
    return sortedlst


if __name__ == "__main__":
    lst = [3, 5, 1, 7, 9, 6, 8]
    print(choicesort(lst))
