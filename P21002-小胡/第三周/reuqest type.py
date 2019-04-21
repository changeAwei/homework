# -*- coding: utf-8 -*-
# @Time  : 2019/4/19 10:25
# @Author : xm11211
# @FileName: reuqest type.py
# @Software: PyCharm
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''

post = logs.lower().count('"post')
get = logs.lower().count('"get')
print('POST:{},GET:{}'.format(post,get))