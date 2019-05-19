#!/usr/bin/env python
# -*- coding: utf-8

import base64

s = 'magedu.com'
code = 'bWFnZWR1LmNvbQ=='


def base64_encoding(s: str) -> str:
    bytes_code = bytes(s, 'utf-8')
    b64_bytes_code = base64.b64encode(bytes_code)
    # print(bytes_code)

    b64_str = str(b64_bytes_code, encoding='utf-8')
    # print(b64_str)
    return b64_str


def base64_decoding(code: str) -> str:
    b64_bytes_code = base64.b64decode(code)
    # print(b64_bytes_code)

    s = str(b64_bytes_code, encoding='utf-8')
    return s


print(base64_encoding(s))
print(base64_decoding(code))
