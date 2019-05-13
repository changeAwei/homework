from functools import lru_cache,wraps
import  inspect
import datetime
def yang_cache(fn):
    local_cache = {}
    @wraps(fn)#wrapper = wraps(fn)(wrapper)
    def wrapper(*args,**kwargs):
        #参数处理，构建key
        sig = inspect.signature(fn)
        params = sig.parameters #有序字典
        params_dict = {}
        #位置传参
        params_dict.update(zip(params.keys(),args))
        #关键字传参
        params_dict.update(kwargs)
        #缺省值
        for k,v in params.items():
            if k not in params_dict:
                params_dict[k] = v.default
        key = tuple(sorted(params_dict.items()))
        print(key)
        if key not in local_cache:
            local_cache[key] = fn(*args,**kwargs)
        print(sig,params,params_dict,local_cache[key])
        return local_cache[key]

    return wrapper

@yang_cache
def add(x=5,y=6):
    return x + y

add()
add(5,6)
add(y=6,x=5)
print(add())