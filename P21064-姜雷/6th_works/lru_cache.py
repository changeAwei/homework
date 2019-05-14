#!/usr/bin/env python

import inspect
import time
import datetime
from functools import wraps


def lru_cache(T):
    def _lru_cache(fn):
        cache = {}

        @wraps(fn)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(fn)
            params = sig.parameters
            params_name = list(params.keys())

            key_dict = {}
            for i, x in enumerate(args):
                key_dict[params_name[i]] = x

            key_dict.update(kwargs)

            key = tuple(key_dict.items())

            def clear_cache(T):
                clear_keys = []
                now = datetime.datetime.now().timestamp()
                for k, (v, t) in cache.items():
                    if now - t > T:
                        clear_keys.append(k)
                for k in clear_keys:
                    cache.pop(k)

            clear_cache(T)

            def make_key():
                if key not in cache.keys():
                    timestamp = datetime.datetime.now().timestamp()
                    value = fn(*args, **kwargs)
                    cache.update({key: (value, timestamp)})
                else:
                    pass
                return cache[key][0]

            return make_key()

        return wrapper

    return _lru_cache


@lru_cache(T=10)  # add = lru_cache(add)(T=1)
def add(x, y=1):
    time.sleep(3)
    value = x + y
    print('hello')
    return value


print(add(4, 1))
print(add(4, 1))
print(add(y=1,x=4))
print(add(4))
# print(datetime.datetime.now().timestamp())
