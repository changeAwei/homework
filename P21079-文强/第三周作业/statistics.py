#有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
#POST 2
#GET 3
#下边是logs变量：
"""
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''
"""
longs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''

s1 = longs.split('\n')
print(s1)
print('~~~~~~~~~~~~~')
s2 = ','.join(s1)
print(s2)
print('~~~~~~~~~~~~~')
s3 = s2.strip(',')
print(s3)
print('~~~~~~~~~~~~~')
s4 = s3.split('"')
print(s4)
print('~~~~~~~~~~~~~')
s5 = ','.join(s4)
print(s5)
print('~~~~~~~~~~~~~')
s6 = s5.upper()
print(s6)
print('~~~~~~~~~~~~~')
POST_num = s6.count('POST /')
print(POST_num)
Get_num = s6.count('GET /')
print(Get_num)
