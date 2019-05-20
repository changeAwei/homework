#2. 使用base64解码“bWFnZWR1LmNvbQ==”，使用base64编码”magedu.com”，分别给出它们的解码和编码结果。
import base64
str1 = "bWFnZWR1LmNvbQ=="
str2 = "magedu.com"
print(base64.b64decode(str1))
print(base64.b64encode(str2.encode('utf-8')))

#4写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html
from pathlib import Path
import os
# p = Path('D:\\tmp')
# f = p.rglob('*.htm')
def change(p,src:str,dest:str):
    x = Path('p')
    f = x.rglob('*src')
    for oldname in f:
        newname = oldname.with_suffix('dest')
        os.rename(oldname,newname)
change('/tmp','.htm','.html')