#������һ���ַ�������logs����ͳ�Ƴ�ÿ���������͵���������ʾ���ո�ָ�ĵ�2�����������ͣ����õ����������
#POST 2
#GET 3
#�±���logs������
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' 
prelogs = logs.replace('\"',' ').upper().split()
numpost = prelogs.count('POST')
numget = prelogs.count('GET')
print('POST num is {}'.format(numpost))
print('GET num is {}'.format(numget))