from functools import wraps
import inspect
import time
def new_cache(fn):
    local_cache = {}
    @wraps(fn) # wraps(fn) -> partial(update_wrapper,wrapped=add(被固定下来))
    # weapper = partial(update_wrapper,wrapper) ->update_wrapper(wrapper)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn) #签名元组
        params = sig.parameters #列表 有序字典-> k-v组成的二元组
        params_dict = {}

        params_dict.update(zip(params.keys(),args)) #更新位置传参
        params_dict.update(kwargs)  #更新关键字传参
        for k,v in params.items():
            if k not in params_dict:
                params_dict[k] = v.default #更新缺省值
        key = tuple(sorted(params_dict.items())) #用元组包一下，否则返回的是一个空列表

        if key not in local_cache.keys():
            local_cache[key] = fn(*args, **kwargs) #计算被包装函数的值
        return local_cache[key]
    return wrapper
@new_cache  #add = wrapper
def add(x, y=5):
    time.sleep(3)
    return x + y

print(add(4,5))
print('~~~~~~~~~~~~~')
print(add(4))
print('~~~~~~~~~~~~~')
print(add(x=4, y=5))
print('~~~~~~~~~~~~~')
print(add(y=5,x=4))
