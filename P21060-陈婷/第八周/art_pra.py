import argparse
from pathlib import Path
def showfile(p:str,shownums=False):
    filename = Path(p)
    n = 1
    with open(filename,'r') as f:
        if shownums:
            for line in f:
                line = str(n) + ' ' +line
                print(line,end = '')
                n +=1
        else:
            for line in f:
                print(line,end = '')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='cat',
                                     description='Concatenate FILE(s), or standard input, to standard output.')
    parser.add_argument('filename')
    parser.add_argument('-n', action='store_true', dest='shownums', help='number all output lines')
    args = parser.parse_args()#

showfile(args.filename,args.shownums)