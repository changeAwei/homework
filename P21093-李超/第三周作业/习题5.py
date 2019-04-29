'''
5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割
的第2列是请求类型），得到如下输出：
POST 2
GET 3
'''


logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''
lst1 = logs.split()

n = len(lst1)
lst2 = lst1[1:n:5]
lst3 = ''.join(lst2).upper().split('"')[1:]
x = lst3.count('POST')
y = lst3.count('GET')
print('POST {}'.format(x))
print('GET {}'.format(y))
