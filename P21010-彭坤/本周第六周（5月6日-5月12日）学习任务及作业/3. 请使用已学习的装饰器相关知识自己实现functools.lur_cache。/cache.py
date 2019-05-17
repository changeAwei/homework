#cache装饰器
from functools import wraps
import inspect
import time
import datetime
from inspect import Parameter
def kg_cache(duration):
    def _cache(fn):
        local_cache = {} 
        @wraps(fn)
        def wrapper(*args, **kwargs): 
            # 清除过期的key
            expire_keys = []
            for k,(_,stamp) in local_cache.items():
                now = datetime.datetime.now().timestamp()
                if now - stamp > duration:
                    expire_keys.append(k)
            for k in expire_keys:
                local_cache.pop(k)
            #参数处理,构建key
            sig = inspect.signature(fn) 
            params = sig.parameters 
            params_names = list(params.keys())
            params_dict = {}
            #可变位置传参
            for i, v in enumerate(args):
                k = params_names[i] 
                params_dict[k] = v
            params_dict.update(kwargs)
            
            #缺省值处理
            for k,v in params.items():
                if k not in params_dict.keys():
                    params_dict[k] = v.default
            key = tuple(sorted(params_dict.items()))
            # 判断是否需要缓存
            if key not in local_cache.keys():
                local_cache[key] = ( fn(*args, **kwargs),
                    datetime.datetime.now().timestamp() ) #时间戳
            return key, local_cache[key]
        return wrapper
    return _cache

def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)
        return ret
    return wrapper

@logger 
@kg_cache(10)
def add(x=4, y=5):
    return x+y

result = []
result.append( add(4, 5) )
result.append(add(4, y=5) )
result.append( add(y=5, x=4))
result.append( add(x=4, y=5))

for x in result:
    print(x)



























