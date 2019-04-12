#! /usr/bin/python36
#1、cat  -n
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='cat',add_help=True,description='check file contents \n $cat file ')
parser.add_argument('file',nargs='?',help='need --file')
parser.add_argument('-n',action='store_true',help="--number\nnumber all output lines")


class Cat_File:
    """
    file: file path
    """

    def __init__(self,file,n=0):
        self.file = file
        self.n = n

    def check_file(self):
        p = Path(self.file)
        if p.name.startswith('.'):
            pass
        else:
            return p.absolute()

    def getfiletype(self):
        path = Path(self.file)
        if path.is_dir():
            return 'd'
        elif path.is_block_device():
            return 'b'
        elif path.is_fifo():
            return 'p'
        elif path.is_file():
            return 'f'
        elif path.is_socket():
            return 's'
        elif path.is_symlink():
            return 'l'
        else:
            return 'other'

def cat_file(file,n=False):
    c = Cat_File(file)
    p = c.check_file()
    mode = c.getfiletype()
    contents = []
    if mode == 'f':
        with p.open() as cf:
            l_file = cf.readlines()
            if not n:
                for i in l_file:
                    contents.append(('  ' + i))

            else:
                for i in l_file:
                    contents.append((str(n) + '  ' + i))
                    n += 1
        for _k in contents:
            print (_k)
    elif mode == 'd':
        return 'please input file name'
    else:
        return 'Non-file types are not executed'


if __name__ == '__main__':
    args = parser.parse_args()
   # print(args)
   # parser.print_help()
    file = cat_file(args.file,args.n)
    print(file)

