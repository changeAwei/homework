#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : add_cache.py
@Author: Lint
@Date  : 2019/4/12 9:27
@Ver   :
@Desc  :
(1)、需求
自定义实现cache装饰器
def add(x=4, y=5):
    time.sleep(3)
    return x + y

以下5种，可以认为是同一种调用
print(1,add(4,5))
print(2,add(4))
print(3,add(y=5))
print(4,add(x=4,y=5))
print(5,add(y=5,x=4))

（2）、分析


"""

from functools import wraps
import inspect
import time
import datetime


def mag_cache(fn):
    local_cache = {}
    @wraps(fn)
    def wrapper(*args, **kwargs):

        # 参数处理，构建key
        sig = inspect.signature(fn)
        params = sig.parameters
        params_dict = {}
        # 位置和关键字传参
        params_dict.update(zip(params.keys(), args))
        params_dict.update(kwargs)
        # 缺省值
        for k, v in params.items():
            if k not in params_dict.keys():
                params_dict[k] = v.default
        key = tuple(sorted(params_dict.items()))
        print(key)

        if key not in local_cache.keys():
            local_cache[key] = fn(*args, **kwargs)
        return local_cache[key]
    return wrapper


@mag_cache
def add(x=4, y=5):
    time.sleep(3)
    return x + y


add()
print("-"*30)
add(4, 5)
print("-"*30)
add(y=5, x=4)
print("-"*30)
