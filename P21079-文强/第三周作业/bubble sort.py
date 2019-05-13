"""
用选择排序算法实现排序  [3, 5, 1, 7, 9, 6, 8]
升序：
使用冒泡法升序排序
"""
nums = [3, 5, 1, 7, 9, 6, 8]
length = len(nums)
for i in range(length):
    for j in range(length - 1 - i):
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
print(nums)
