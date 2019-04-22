##4.使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]

####代码开始####
a = [3,5,1,7,9,6,8,5,6,7]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

####代码结束####





 
#5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到
#如下输出：
#POST 2
#GET 3

#下边是logs变量：
#logs = '''
#111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
#111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
#111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
#223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
#111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
#'''

####代码开始####


logs='''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
####子串搜索####
##HTTP/URL 操作方式 基础知识##
# HTTP协议中共定义了八种方法或者叫“动作”来表明对Request-URI指定的资源的不同操作方式，具体介绍如下： 

# OPTIONS：返回服务器针对特定资源所支持的HTTP请求方法。也可以利用向Web服务器发送'*'的请求来测试服务器的功能性。 
# HEAD：向服务器索要与GET请求相一致的响应，只不过响应体将不会被返回。这一方法可以在不必传输整个响应内容的情况下，就可以获取包含在响应消息头中的元信息。 
# GET：向特定的资源发出请求。 
# POST：向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的创建和/或已有资源的修改。 
# PUT：向指定资源位置上传其最新内容。 
# DELETE：请求服务器删除Request-URI所标识的资源。 
# TRACE：回显服务器收到的请求，主要用于测试或诊断。 
# CONNECT：HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。

#    虽然HTTP的请求方式有8种，但是我们在实际应用中常用的也就是get和post，其他请求方式也都可以通过这两种方式间接的来实现。
#https://www.cnblogs.com/web100/p/http-8-request.html    
#开辟8个HTTP请求方法的列表
a=["POST","GET","HEAD","PUT","OPTIONS","DELETE","TRACE","CONNECT"]
#开辟8个请求方法类表的初始值
b=[0,0,0,0,0,0,0,0]
#准备一个接受切割后的字符容器
c=[None]
#对待处理字符串，全大写，并分割字符串为列表
list_c =logs.upper().split()
#计算承接容器的长度
length=int(len(list_c)/5)
#开启固定长度的容器
c=c*length

#获取感兴趣的参数
for x in range(length):
    #这里刚好有个规律，1+5n处刚好是我想要的初始数据，用字符串切割lstrip把多余的部分去掉
    c[x]=((list_c[1+5*x]).lstrip('"') )
#这个输出核查一下是否是自己想要的数据
#print(c)

#这里统计一下每个方法的次数
for i in range(8):
    for j in range(length):
         if a[i]==c[j]:
                b[i]+=1
    #借助for循环打印我想要的输出的信息
    if b[i]!=0:
        print(a[i],b[i])
####代码结束###
