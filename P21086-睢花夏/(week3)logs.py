logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
log1 = logs.replace('Get','GET')
log2 = log1.replace('Post','POST')
log3 = log2.split()
#print('POST',log3.count('"POST'))
#print('GET',log3.count('"GET'))
print(' POST {} \n GET {}'.format(log3.count('"POST'),log3.count('"GET')))
