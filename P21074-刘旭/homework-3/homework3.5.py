# 5\有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
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
lst_logs = logs.replace( '"',' ').upper().split()
#print(lst_logs)
a = lst_logs.count('POST')
b = lst_logs.count('GET')
print('POST:{}'.format(a))
print('GET:{}'.format(b))

#优化方向应该是减少遍历次数，想好了再继续优化