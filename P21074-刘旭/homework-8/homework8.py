#1. 使用本周和之前所学习的知识实现cat命令（支持查看内容和-n参数功能即可）
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='cat',description='This program prints files to the standard output.')
parser.add_argument('path',action='store_true')
parser.add_argument('-n',action='store_true')
def readfile(path:str,n=False):
    p = Path(path)
    if p.is_file():
        with open(p) as f:
            for line in f:
                print(line)
        if not n:
            with open(p) as f:
                for i,line in enumerate(f,1):
                    print(i,line)
    elif p.is_dir() and p.exists():
        print('path:Is a directory')
    else:
        print('No such file or directory')
if __name__ == '__main__':#这下面的东西没搞太懂，看了下视频还是比较懵
    args = parser.parse_args()
    print(args)

#2. 有字符串”not 404 found 张三 99 深圳”，使用正则过滤掉英文和数字，最终得到”张三 深圳”
import re
test = 'not 404 found 张三 99 深圳'
pattern = '[^a-z0-9]+'
regex = re.compile(pattern)
matcher = regex.findall(test)
print(''.join(matcher).strip())
