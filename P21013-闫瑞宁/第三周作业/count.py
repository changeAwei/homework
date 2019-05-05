logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
count_POST = 0
count_GET = 0
logs_list = logs.split('\n')
for i in logs_list:
    if i.upper().find('POST') != -1 and i.upper().find('POST')<20:
        count_POST += 1
    if i.upper().find('GET') != -1 and i.upper().find('GET')<20:
        count_GET += 1
print('POST',count_POST)
print('GET',count_GET)
