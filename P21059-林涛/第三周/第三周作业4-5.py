'''4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]'''

#一元选择排序（简单排序）
nums = [3, 5, 1, 7, 9, 6, 8]
length = len(nums)
for i in range(length - 1):
    maxindex = i
    for j in range(i + 1,length):
        if nums[j] < nums[maxindex]:
            maxindex = j
    if maxindex != i:
        nums[i],nums[maxindex] = nums[maxindex],nums[i]
print(nums)

############################################

#Bubble sort 冒泡法排序
nums = [3, 5, 1, 7, 9, 6, 8]
length = len(nums)
flag = False #打标签，顺序相同提前结束。优化点
for i in range(length):
    for j in range(length -1- i):
        if nums[j] > nums[j+1]:
            #prenums = nums[j]
            #nums[j] = nums[j+1]
            #nums[j+1] = prenums
            nums[j],nums[j+1] = nums[j+1],nums[j] #交换
            flag = True
    if not flag:
            break            
print(nums)

"""
5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
POST 2
GET 3
下边是logs变量：
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' """
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''

postcount = logs.lower().count('"post')
getcount = logs.upper().count('"GET')
print('POST:{},GET:{}'.format(postcount,getcount))

#print('POST:{},GET:{}'.format(logs.lower().count('"post'),logs.upper().count('"GET')))
