#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2019/5/26 14:59
# @Author : Fly
# @FileName: 第八周作业.py
# @Software: PyCharm
#实现Cat命令
from pathlib import Path
p = Path('/tmp')
def Mycat(Path,Letter='n'): #定义函数传入参数,文件路径及n参数
    if Letter =='n':#如果需要n参数
        if Path.is_file():#如果路径最后是文件
            file = open(Path.name,'r')#只读模式打开
            for lens,content in enumerate(file)#用枚举获取行数及内容
                print(lens,content)#行数和内容同步打印
            file.close()#关闭文件
        else:
            print(Path.name+' '+ 'is dir')#不是文件则显示为目录
    else:#如果不传入n参数
        if Path.is_file():
            file = open(Path.name,'r')
            print(file.read())#只打印文件内容
        else:
            print(Path.name + ' ' + 'is dir')#不是文件则显示为目录

#有字符串”not 404 found 张三 99 深圳”，使用正则过滤掉英文和数字，最终得到”张三 深圳”

import re
s = "not 404 found 张三 99 深圳"
lst = s.split(" ")                            # ['not', '404', 'found', '张三', '99', '深圳']
nolst = re.findall("\d+|[a-zA-Z]+", s)        # ['not', '404', 'found', '99']
tmp = [x for x in lst if not x in nolst]      # ['张三', '深圳']
print(" ".join(tmp))                          # 张三 深圳
