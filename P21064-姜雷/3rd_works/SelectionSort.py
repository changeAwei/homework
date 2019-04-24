#!/usr/bin/env python


l = [3, 5, 1, 7, 9, 6, 8]

length = len(l)

count = 0
swap = 0
for i in range(length):
    max = i
    for j in range(i + 1, length):
        if l[max] < l[j]:
            max = j
            count += 1
    if max != i:
        l[i], l[max] = l[max], l[i]
        swap += 1

print(l)
print(count, swap)
