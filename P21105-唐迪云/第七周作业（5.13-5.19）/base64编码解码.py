##使用base64解码“bWFnZWR1LmNvbQ==”，使用base64编码”magedu.com”，分别给出它们的解码和编码结果

import base64
str1 = 'bWFnZWR1LmNvbQ=='
print(base64.b64decode(str1).decode( 'utf-8' ))

import base64
str2 = 'magedu.com'
print(base64.b64encode(str2).encode( 'utf-8' ))