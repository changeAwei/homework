import time
import inspect
from functools import wraps

def hua_cache(fn):
    local_cache = {} # 对不同函数名是不同的cache

    @wraps(fn)
    def wrapper(*args, **kwargs):  # 接收各种参数,kwargs普通字典参数无序
        # 参数处理，构建key
        sig = inspect.signature(fn)
        params = sig.parameters  # 只读有序字典

        param_names = [key for key in params.keys()]
        params_dict = {}
        for i, v in enumerate(args):
            k = param_names[i]
            params_dict[k] = v

        params_dict.update(kwargs)

        # 缺省值处理
        for k,v in params.items():
            if k not in params_dict.keys():
                params_dict[k] = v.default

        key = tuple(sorted(params_dict.items()))
        # 判断是否需要缓存
        if key not in local_cache:
            local_cache[key] = fn(*args, **kwargs)
        return key, local_cache[key]
    return wrapper
@hua_cache
def add(x, z, y=6):
    time.sleep(3)
    return x + y + z

print(add(4, 5))
print('~~~~~~~~~~~~~')
print(add(4, z=5))
print('~~~~~~~~~~~~~~')
print(add(4, y=6, z=5))
print('~~~~~~~~~~~~~')
print(add(y=6, z=5, x=4))
print('~~~~~~~~~~~~~~~')
print(add(4, 5, 6))











