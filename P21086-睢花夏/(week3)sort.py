1.
num = [3,5,1,7,9,6,8]
length = len(num)

for i in range(length):
    for j in range(length-i-1):
        if num[j] < num[j+1]:
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1] = tmp
print(num)


2.
num = [3,5,1,7,9,6,8]
length = len(num)

for i in range(length):
    for j in range(length-i-1):
        if num[j] < num[j+1]:
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1] = tmp
print(num)


3.
num = [3,5,1,7,9,6,8]
num.sort()
print(num)

4.
num = [3,5,1,7,9,6,8]
num.sort(reverse=True)
print(num)

5.
#封装与解构
num = [3,5,1,7,9,6,8]
length = len(num)

for i in range(length):
    for j in range(length-i-1):
        if num[j] < num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]
print(num)
