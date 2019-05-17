# 1. 内置的open函数打开文件有几种模式，它们的区别是什么？
'''
	r	缺省的，表示只读打开
	w	只写打开
	x	创建并写入一个新文件
	a	写入打开，如果文件存在，则追加
	b	二进制模式
	t	缺省的，文本模式
	+	读写打开一个文件，给原来只读、只写方式打开提供确实的读或者写的能力
'''

# 2. 使用base64解码“bWFnZWR1LmNvbQ==”，使用base64编码”magedu.com”，分别给出它们的解码和编码结果。
import base64

s1='bWFnZWR1LmNvbQ=='
base64_decrypt = base64.b64decode(s1.encode('utf-8'))
print(str(base64_decrypt,'utf-8'))
print('-'*30)
s2='magedu.com'
base64_encrypt = base64.b64encode(s2.encode('utf-8'))
print(str(base64_encrypt,'utf-8'))


# 3. 列出本周讲的几种序列化方法，它们各自的特点是什么？
'''
pickle库：Python中的序列化、反序列化模块，在Python程序之间可以用其解决序列化与反序列化问题，
    如果是跨平台、跨语言、跨协议pickle不合适。需要使用公共协议。例如XML、Json、Protocol Buffer。
    
Json：是一种轻量级的数据交换格式。它基于EMCAScript的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。
    一般Json编码的数据很少落地，数据都是通过网络传输。Json很简单，几乎语言编程都支持Json，所以应用范围十分广泛。
    
MessagePack：是一个基于二进制高效的对象序列化类库，可用于跨语言通信。它可以向Json那样，在许多语言之间交换结构对象。
    但它比Json更快速也更轻巧。支持Python、Java等众多语言。兼容Json和pickle。MessagePack简单易用，高效压缩，支持语言丰富。
'''

# 4. 写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html
from pathlib import Path
import os

p = Path('d:/tmp')
def replace_suffix(p:Path):
    for x in p.iterdir():
        if x.is_dir():
            replace_suffix(x)
        elif x.suffix == '.htm':
            os.rename(str(x),Path(x).with_suffix('.html'))

replace_suffix(p)
