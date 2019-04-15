# 4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
lst = [3, 5, 1, 7, 9, 6, 8]
length = len(lst)
for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if lst[maxindex] < lst[j]:
            maxindex = j

    if i != maxindex:
        temp =lst[i]
        lst[i] = lst[maxindex]
        lst[maxindex] = temp

print(lst)

# 5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
# POST 2
# GET 3
# 下边是logs变量：
# logs = '''
# 111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
# 111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
# 111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
# 223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
# 111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
# '''
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
lst = logs.replace('"',' ').split()
dic = {}
for i in lst:
    dic[i.upper()] = dic.get(i.upper(),0) + 1

print('POST:{}'.format(dic['POST']))
print('GET:{}'.format(dic['GET']))
