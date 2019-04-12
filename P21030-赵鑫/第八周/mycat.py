#1. 使用本周和之前所学习的知识实现cat命令（支持查看内容和-n参数功能即可）
import argparse
class Mycat:
    def __init__(self,file,number=False):
        self.file = file
        self.number = number

    def filecontents(self):
        with open(self.file) as f:
            if self.number:
                for i, line in enumerate(f):
                    print(i + 1, line, end='')
            else:
                for line in f:
                    print(line,end='')

parse = argparse.ArgumentParser(prog='cat',add_help=True,description='Display file contents')
parse.add_argument('file',nargs='?')
parse.add_argument('-n','-number',action='store_true',help='Number all lines of output starting with 1')
args = parse.parse_args('d:/tmp/123.txt -n'.split())

c = Mycat(args.file,args.n)
c.filecontents()
