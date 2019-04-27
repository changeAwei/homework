

#### 1.深拷贝和浅拷贝区别 
```
浅拷贝：复制了外围的对象，但是里面的引用没用复制
深拷贝：把对象复制一遍，里面的引用也复制了一遍
```



####2. 说明列表和元组的相同点和不同点

```
相同点：
1.都属于有序序列
不同点：
1.元祖属于不可变序列，一旦创建，则不可修改
2.元祖可当做字典的键或者集合中的元素，列表不可做字典的键和集合中的元素

```







#### 3.请写出字符串支持的所有方法及说明（例如: lower 返回字符串的小写）

```
1、eval(string)
将字符串string当成有效的表达式来求值并返回计算结果。
2、len(string)
返回字符串的长度(字符个数)。
3、lower(string)
转换字符串种大写字母为小写字母。
4、upper()
转换字符串中小写字母为大写字母。
5、swapcase()
转换字符串中的小写字母为大写字母，大写字母为小写字母。
6、capitalize()
字符串首字母大写，其他小写。
7、title()
每个单词的首字母大写。
8、center(width, fillchar)
返回一个指定宽度的居中字符串，fillchar为填充字符，默认空格填充。
9、ljust(width[, fillchar])
返回一个指定宽度的左对齐字符串，fillchar为填充字符，默认空格填充。
10、rjust(width[, fillchar])
返回一个指定宽度的右对齐字符串，fillchar为填充字符，默认空格填充。
11、zfill(width)
返回一个长度为width的字符串，原字符串右对齐，前面补0。
12、count(str[, star][, end])
返回字符串中str出现的次数，可以指定一个范围，默认从头至尾。
13、find(str[, star][, end])
从左往右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，得到的是第一次出现的开始下标，没有则返回-1。
14、rfind(str[, stat][, end])
15、index(str, star=0, end=len(str)
和find()一样，只不过如果str不存在的时候回报一个异常。
15、lstrip()
截掉字符串左侧指定的字符，默认为空格
16、rstrip()
截掉字符串右侧指定的字符，默认为空格。
17、strip()
截掉字符串两侧指定的字符。
18、split(str, num)
以str为分割符截取字符串，指定num，则仅截取num个字符串。
19、splitline([keepends])
按照（‘\r’，‘\r\n’，‘\n’）分隔（按行切割），keepend==true 会保留换行符。
20、join(seq)
以指定的字符串分隔符，将seq中的所有元素组合成一个字符串。
21、replace(oldstr, newstr, count)
用newstr替换oldstr，默认是全部替换。如果指定了count，则只替换前count个。
22、encode(encoding="utf-8", error="strict")
以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
23、isalpha()
如果字符串中至少有一个字符且所有的字符都是字母，返回True，否则返回False。
24、isalnum()
如果字符串中至少有一个字符且所有的字符都是字母或数字，返回True，否则返回False。
25、isupper()
如果字符串中至少有一个英文字符且所有的英文字符都是大写字母，返回True，否则返回False。
26、islower()
如果字符串中至少有一个英文字符且所有的英文字符都是小写字母，返回True，否则返回False。
27、istitle()
如果字符串是标题化的返回True，否则返回False。
28、isdigit()
如果字符串中只包含数字字符返回True，否则返回False。

```







#### 4.使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]

```
#!/usr/bin/python
# -*- coding:utf-8 -*-

def select(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]
    return list
if __name__ == "__main__":
    origin_list = [3, 5, 1, 7, 9, 6, 8]

    print select(origin_list)
```



####5.有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型）

```python
#!/usr/bin/python
# -*- coding:utf-8 -*-


logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
'''


def get_key_list(para1):
    key_list = []
    if len(para1) == 0:
        return key_list
    else:
        for i in para1.split('\n'):
            i_list = i.split('"')
            if len(i_list) > 1:
                k = i_list[1].split(' ')[0]
                key_list.append(k)
        return key_list

def ana(list1):
    ana_dict = {}
    for i in list1:
        if i.upper() not in ana_dict.keys():
            ana_dict[i.upper()] = 1
        else:
            ana_dict[i.upper()] += 1

    return ana_dict


if __name__ == "__main__":
    ana_list = get_key_list(logs)
    ana_dict = ana(ana_list)
    for k in ana_dict:
        print k, ana_dict[k]
```
