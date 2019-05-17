# -*- coding: utf-8 -*-
# @Time  : 2019/5/14 10:24
# @Author : xm11211
# @FileName: lur_cache.py
# @Software: PyCharm
import time
import inspect
import datetime
from functools import wraps
def mag_cache(duration = 5):
    def _mag_cache(fn):
        local_cache = {} # 对不同函数名是不同的cache
        @wraps(fn)
        def wrapper(*args, **kwargs): # 接收各种参数,kwargs普通字典参数无序
            def _clear_expire():
                expire_keys = []
                for k,(_,stamp) in local_cache.items():
                    if datetime.datetime.now().timestamp() - stamp > duration:
                        expire_keys.append(k)
                for i in expire_keys:
                    del local_cache[i]

            def _make_keys(args, kwargs):
                # 参数处理，构建key
                params_dict = {}
                sig = inspect.signature(fn)
                params = sig.parameters  # 只读有序字典
                # 位置参数
                # keys = list(params.keys())
                # for i, v in enumerate(args):
                #     params_dict[keys[i]] = v
                params_dict.update(zip(params.keys(), args))
                # for k, v in kwargs.items():
                #     params_dict[k] = v
                # 关键字参数
                params_dict.update(kwargs)
                # 缺省值处理
                for k, v in params.items():
                    if k not in params_dict.keys():
                        params_dict[k] = v.default
                key = tuple(sorted(params_dict.items()))
                return key

            _clear_expire()
            key = _make_keys(args, kwargs)
            # 判断是否需要缓存
            if key not in local_cache.keys():
                local_cache[key] = fn(*args, **kwargs), datetime.datetime.now().timestamp()
            print(local_cache)
            return key, local_cache[key]
        return wrapper
    return _mag_cache
@mag_cache(10)
def add(x, z, y=6):
    time.sleep(3)
    return x + y + z
result = []
result.append(add(4, 5))
result.append(add(4, z=5))
result.append(add(4, y=6, z=5))