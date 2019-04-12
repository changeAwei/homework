# 4. 写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html

from pathlib import Path
import os

f = Path('./tmp')
fpaths = f.rglob('*.htm')
for fpath in fpaths:
    newname = fpath.with_suffix('.html')
    os.rename(fpath, newname)