1.说明列表的浅拷贝和深拷贝的区别
{
浅拷贝:又叫影子拷贝，只是复制引用，其列表的内存地址，值的信息都是一样的，一个修改则另一个一起被修改。
深拷贝:对源列表的完整复制，相当于创建一个新的列表，两个列表互不影响。
}
2.说明列表和元组的相同点和不同点
{
共同点：都可以通过索引查询到某个元素，可以切片
不同点：列表元素是可变，元组中元素不可变
}
3.请写出字符串支持的所有方法及说明（例如:lower返回字符串的小写）
{
capitalize()                              把字符串的第一个字符改为大写 
casefold()                                把整个字符串的所有字符改为小写
center(width)                             将字符串居中，并使用空格填充至长度width的新字符串，效果就是居中显示了，两边是空格
ljust(width)                              返回一个左对齐的字符串，并使用空格填充至长度为width的新字符串。
rjust(width)                              返回一个右对齐的字符串，并使用空格填充至长度为width的新字符串。
count(sub[,start[,end]])                  返回sub在字符串里边出现的次数，start和end参数表示范围，可选,多用来统计。
encode(encoding='utf-8', errors='strict') 以encoding指定的编码格式对字符串进行编码。
startswith(prefix[,start[,end]])          检查字符串是否以prefix开头，是则返回True，否则返回False。start和end参数可以指定范围检查，可选。
endswith(sub[,start[,end]])               检查字符串是否以sub子字符串结束，如果是返回True，否则返回False。start和end参数表示范围，可选。
expandtabs([tabsize=8])                   把字符串中的tab符号（\t）转换为空格，如不指定参数，默认的空格数是tabsize=8，用来人为的控制 \t 的距离。
find(sub[,start[,end]])                   检测sub是否包含在字符串中，如果有则返回索引值，否则返回-1，start和end参数表示范围，可选，用来检测sub所在的位置。
rfind(sub[,start[,end]])                  类似于find()方法，不过是从右边开始查找。
index(sub[,start[,end]])                  跟find方法一样，不过如果sub不在string中会产生一个异常。
rindex(sub[,start[,end]])                 类似于index()方法，不过是从右边开始。
isalnum                                   如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False。
isalpha()                                 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False。
isdecimal()                               如果字符串只包含十进制数字则返回True，否则返回False。
isdigit()                                 如果字符串只包含数字则返回True，否则返回False。
islower()                                 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True，否则返回False。
isupper()                                 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回True，否则返回False
isnumeric()                               如果字符串中只包含数字字符，则返回True，否则返回False。
isspace()                                 如果字符串中只包含空格，则返回True，否则返回False。
title()                                   返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串。
istitle()                                 如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回True，否则返回False。
join(sub)                                 以字符串作为分隔符，插入到sub中所有的字符之间，让字符串以字符为单位分开，字符间插入sub。
swapcase()                                翻转字符串中的大小写。
lower()                                   转换字符串中所有大写字符为小写。
upper()                                   转换字符串中的所有小写字符为大写。
strip([chars])                            删除字符串前边和后边所有的空格，chars参数可以定制删除的字符，可选。
lstrip()                                  去掉字符串左边的所有空格
rstrip()                                  删除字符串末尾的空格。
partition(sub)                            找到子字符串sub，把字符串分成一个3元组（pre_sub,sub,fol_sub），如果字符串中不包含sub则返回(‘原字符串’, ’’, ’’)，简单来说就是将字符串分为三部分，sub前面，sub，sub后面然后生成一个元组。
rpartition(sub)                           类似于partition()方法，不过是从右边开始查找。
replace(old,new[,count])                  把字符串中的old子字符串替换成new子字符串，如果count指定，则替换不超过count次。
split(sep=None,  maxsplit=-1)             不带参数默认是以空格为分隔符切片字符串，如果maxsplit参数有设置，则仅分隔maxsplit个子字符串，返回切片后的子字符串拼接的列表。
splitlines(([keepends]))                  按照‘\n’分隔，返回一个包含各行作为元素的列表，如果keepends参数指定，则返回前keepends行。
translate(table)                          根据table的规则（可以由str.maketrans(‘a’,‘b’)定制）转换字符串中的字符。
zfill(width)                              返回长度为width的字符串，原字符串右对齐，前边用0填充，若字符串长度小于width，则前端用0来进行填充
}
4.使用选择排序算法实现排序[3,5,1,7,9,6,8]
{
#冒泡排序就是遍历数据，每次只与下一个数字比较，如果这两个数顺序不对，则与交换过来。
#选择排序从0位置开始与后面每个数比较，条件成立就交换
a = [3, 5, 1, 7, 9, 6, 8]
for i in range(len(a)-1):  #0-5  第一次 0
    min_index = i       # 0
    for j in range(i+1,len(a)): #1-6  第一次a[0]依次 1 2 3 4 5 6比较大小  第二次 a[1] 依次2 - 6 比较大小
        if a[min_index] > a[j]: # 依次比较，条件成立重置索引  第一次成立是 a[2]   第二次 是a[2]
            min_index = j  
            print(j)
    a[i],a[min_index] = a[min_index],a[i] #每次找出最小值并交换位置 第一次[1, 5, 3, 7, 9, 6, 8] 第二次[1, 3, 5, 7, 9, 6, 8]
print(a)
}

5.有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
POST 2
GET 3
{
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''
postnumber ='POST ' +  str(logs.upper().count('"POST'))
getnumber ='GET ' +  str(logs.upper().count('"GET'))
print("%s\n%s" %(postnumber,getnumber))
}