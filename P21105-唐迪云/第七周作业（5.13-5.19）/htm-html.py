##写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html
from pathlib import Path
import os
files = os.listdir( "/tmp" )  # 获取当前目录下的文件
for filename in files:
    portion = os.path.splitext(filename)  # 将文件名拆成名字和后缀
    print(portion)
    if portion[1] == ".htm":  # 关于后缀
        newname = portion[0] + ".html"
