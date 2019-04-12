#!/usr/bin/env python
# -*- coding: utf-8

import re

s = " not 404 found 张三 99 深圳"

regex = re.compile("[^0-9a-zA-Z]+")
result = regex.finditer(s)

print(''.join(map(lambda x:x.group(), result)))



