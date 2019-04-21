#!/usr/bin/env python
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' 
list_logs=logs.strip().splitlines()
list_meth=[]
for i in list_logs:
    list_meth.append(i.split()[1].replace('"','').upper())
list_tmp=[]

for i in list_meth:
    if i not in list_tmp:
        print('{}\t{}'.format(i,list_meth.count(i)))
        list_tmp.append(i)
