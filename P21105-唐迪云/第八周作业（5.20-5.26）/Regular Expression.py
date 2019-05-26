### 有字符串”not 404 found 张三 99 深圳”，使用正则过滤掉英文和数字，最终得到”张三 深圳”

## 方法一：将字符串转变成列表，根据正则匹配到数字和英文字符，然后从列表中移除，用join重新拼接字符串

import re
S = "not 404 found 张三 99 深圳"
L = S.split(" ")                              # ['not', '404', 'found', '张三', '99', '深圳']
res = re.findall("\d+|[a-zA-Z]+", S)          # ['not', '404', 'found', '99']
tmp = [item for item in L if not item in res] # ['张三', '深圳']
print(" ".join(tmp))                          # 张三 深圳

## 方法二：以英文字符和数字作为分隔符，得到一个空字符和中文的列表，再用join来拼接

import re
S = "not 404 found 张三 99 深圳"
L = re.split("[\d+|(a-z)+]", S)  # ['', '', '', ' ', '', '', ' ', '', '', '', '', ' 张三 ', '', ' 深圳']
print("".join(L).strip())        # 张三 深圳
