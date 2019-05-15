#写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html
from pathlib import Path
p = Path('/tmp')
g = p.rglob('*.htm')

for x in g:
    print(p.with_suffix('.html'))