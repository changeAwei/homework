logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''

logs = logs.strip(' \n')                   #去掉头尾空格和换行符
dict = {}                                  #初始化字典
while logs.partition('\n')[0] != '':       #对 logs逐行迭代
    line = logs.partition('\n')[0]
    logs = logs.partition('\n')[2]
    line = line.partition(' ')[2]          #取出该行字符串，并更新logs
    word = line.partition(' ')[0]
    word = word.strip('"')
    word = word.upper()                    #取出该行中请求命令的字符串，去除无用的引号并设为大写
    flag = False                           #初始化flag，表示字典中是否存在该命令
    for key in dict:
        if key == word:
            flag = True
            break
    if dict != {} and flag == True:
        dict.update({word: dict[word]+1})  #存在时，加一
    else:
        dict.update({word: 1})             #不存在时，增加该键
for(key,value) in dict.items():
    print(key + ' ' + str(value))          #打印该字典