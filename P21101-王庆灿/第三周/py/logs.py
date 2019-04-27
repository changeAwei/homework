logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
# print(logs)
logs = logs.lstrip().splitlines()
result = [['POST', 0], ['Get', 0]]
for i in logs:
    if i.find('POST') != -1:
        result[0][1] += 1
    else:
        result[1][1] += 1
for i in range(len(result)):
    print("{:<4}   {:<10}".format(result[i][0], result[i][1]))
