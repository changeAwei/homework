logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
log_lst = logs.split('\n')                #以换行符 "\n"进行切割，获得了一个 n(行数) + 2 个元素的列表。
post_count = 0
get_count = 0
for i in range(1,len(log_lst)-1):
    kwd = log_lst[i].split('"')[1].split(' ')[0].upper()
    if kwd == 'POST':
        post_count += 1
    elif kwd == 'GET':
        get_count += 1
print("POST:",post_count)
print("GET:",get_count)