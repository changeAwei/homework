str1 = "not 404 found 张三 99 深圳" #过滤掉英文和数字，最终得到”张三 深圳”

import re
re_rule = re.compile(r'[^a-z 0-9]+')
re_rule.findall(str1)
