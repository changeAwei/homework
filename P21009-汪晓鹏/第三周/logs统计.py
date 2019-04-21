# 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
# POST 2
# GET 3

logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''

line = logs.strip().split('\n')
dic = {}
for row in line:
    cell = row.split()
    type = cell[1].lstrip('"').upper()
    dic[type] = dic.get(type, 0) + 1
print(dic)

