# 4、使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
nums = [3, 5, 1, 7, 9, 6, 8]
length = len(nums)
for i in range(length):
    flag = False  # 某一趟不用交换 就结束
    for j in range(length-1-i):
        if nums[j] > nums [j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            #nums[j],nums[j+1] = nums[j+1],nums[j]
            flag = True
    if not flag:
        break
print(nums)




