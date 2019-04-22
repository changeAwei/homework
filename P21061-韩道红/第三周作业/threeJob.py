# 1. 说明列表的浅拷贝和深拷贝的区别
"""
浅拷贝: 通过copy模块里面的浅拷贝函数copy()，对指定的对象进行浅拷贝,浅拷贝会创建一个新的对象,
但是，对于对象中的元素，浅拷贝就只会使用原始元素的引用.
深拷贝: 通过copy模块里面的深拷贝函数deepcopy()，对指定的对象进行深拷贝,跟浅拷贝类似，
深拷贝也会创建一个新的对象,但是，对于对象中的元素，深拷贝都会重新生成一份，而不是简单的使用原始元素的引用
"""
# 2. 说明列表和元组的相同点和不同点
"""
1.列表属于可变序列，他的元素可以随时修改或删除；元组属于不可变序列，其中的元素不可以修改，除非整体替换。
2.列表可以使用append()、extend()、insert()、remove()、pop()等方法实现添加和修改列表元素，
而元组没有这几个方法，所以不能想元祖中添加和修改元素。同样，元组也不能删除元素。
3.列表可以使用切片访问和修改列表中的元素。元组也支持切片，但是他只支持通过切片访问元素，不支持修改。
4.元组比列表的访问和处理速度快，所以只是需要对其中的元素进行访问，而不进行任何修改时，建议使用元组。
5.列表不能为字典的键，而元组可以。
"""
# 3. 请写出字符串支持的所有方法及说明（例如: lower 返回字符串的小写）
"""
1.capitalize 把字符串第一个字母大写.
2.center(width) 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串.
3.count(str) 返回str在字符串中出现的个数.
4.decode 指定字符串的解码
5.encode 指定字符串的编码
6.endswith(obj) 指定字符串是否以obj结束
7.find(str) 检测 str 是否包含在字符串中,如果是返回第一个找到的索引值,否则返回 -1
8.format() 字符串格式化
9.index(str) 跟find()方法类似,但是如果str不存在字符串中,会报一个异常
10.isalnum 字符串字符是否全部是字母或全部是数字返回 True,否则返回 False
11.isalpnum 字符串是否包含数字很字母的混合返回True,否则返回False
12.isdecimal 字符串只包含十进制数字则返回 True 否则返回 False
13.isdigit 字符串只包含数字则返回 True 否则返回 False.
14.' '.join(seq) 以' '作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
15.lower 转换 string 中所有大写字符为小写.
16.lstrip 截掉 string 左边的空格
17.replace(str1, str2, num=string.count(str1)) 把字符串中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次
18.rfind 类似于 find()函数，不过是从右边开始查找.
19.rindex 类似于 index()，不过是从右边开始.
20.rstrip  删除 string 字符串末尾的空格.
21.split(str="", num=string.count(str)) 以 str 为分隔符切片字符串，如果 num 有指定值，则仅分隔 num+ 个子字符串
22.startswith(obj, beg=0,end=len(string)) 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
23.swapcase 翻转 string 中的大小写
24.upper 转换字符串中的小写字母为大写
25.string[:10] 截取字符串
26.len(string) 计算字符串长度
 """
# 4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
the_list=[3, 5, 1, 7, 9, 6, 8]
i = 0
while i < len(the_list):
    j = i+1
    while j < len(the_list):
        if the_list[i] > the_list[j]:
            the_list[i], the_list[j] = the_list[j], the_list[i]
        j = j+1
    i = i+1
print(the_list)
# 5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
# POST 2
# GET 3
# 下边是logs变量：
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''
strs = logs.upper().strip().split('\n')
POST,GET = 0,0
for i in strs:
    if i[:30].find('POST') != -1:
        POST += 1
    else:
        GET += 1
print("POST: ",POST)
print("GET: ",GET)
