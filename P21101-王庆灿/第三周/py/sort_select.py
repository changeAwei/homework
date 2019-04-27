tar0 = [3, 5, 1, 7, 9, 6, 8]
tar1 = [0] * 7
j = 0
while tar0:
    ma = tar0[0]
    count = 0
    for i in range(1, len(tar0)):
        if tar0[i] > ma:
            ma = tar0[i]
            count = i
    tar1[j] = ma
    j += 1
    tar0.pop(count)
print(tar1)
