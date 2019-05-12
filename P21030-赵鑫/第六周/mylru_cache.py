import inspect
import time
from functools import wraps
import datetime

def mag_cache(duration):
    def _cache(fn):
        local_cache = {}
        @wraps(fn)
        def wrapper(*args,**kwargs):
            def clear_expire(cache):
                for k,(_,stamp) in cache.items():
                    now = datetime.datetime.now().timestamp()
                    if now - stamp > duration:
                        cache.pop(k)
            clear_expire(local_cache)
            
            def make_key():
                sig = inspect.signature(fn)
                params:dict = sig.parameters
                params_name = [key for key in params.keys()]
                params_dict = {}
                for i,v in enumerate(args):
                    params_dict[params_name[i]] = v
                params_dict.update(kwargs)
                for k,v in params.items():
                    if k not in params_dict.keys():
                        params_dict[k] = v.default
                return tuple(sorted(params_dict.items()))

            key = make_key()
            if key not in local_cache.keys():
                local_cache[key] = (fn(*args,**kwargs),datetime.datetime.now().timestamp())
            return key,local_cache[key]
        return wrapper
    return _cache
    
@mag_cache(10)
def add(x,y,z=6):
    time.sleep(2)
    return x + y + z

print(add(2,3))
print('-'*30)
print(add(x=2,y=3))
print('-'*30)
print(add(2,y=3))
