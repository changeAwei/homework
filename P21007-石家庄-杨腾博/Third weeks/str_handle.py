logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''
#1.
lower = logs.lower()
post = lower.count('"post')
get = lower.count('"get')
print('方法1:','POST {}\t\tGET {}'.format(post,get))

#2.
a = lower.split()
post2 = 0
get2 = 0
for i in a:
    if i.startswith('post',1):
        post2 += 1
    if i.startswith('get',1):
        get2 += 1
print('方法2:','POST {}\t\tGET {}'.format(post2,get2))




# intab = "aeiou"
# outtab = "12345"
# deltab = "thw"
# trantab1 = str.maketrans(intab, outtab)  # 创建字符映射转换表
# trantab2 = str.maketrans(intab, outtab, deltab)  # 创建字符映射转换表，并删除指定字符
# test = "this is string example....wow!!!"
# print(test.translate(trantab1))
# print(test.translate(trantab2))