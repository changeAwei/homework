#!/usr/bin/env python
l=[3, 5, 1, 7, 9, 6, 8]
length=len(l)
for i in range(length-1):
    Flag=True
    for j in range(length-i-1):
        if l[j] > l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            Flag=False
    print(l)
    if Flag:
        break
print(l)
