from functools import wraps
import time
import inspect
def new_cache(fn):
    local_cache = {}
    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters

        param_names = [key for key in params.keys()]
        params_dict = {}
        for i, v in enumerate(args):
            k = param_names[i]
            params_dict[k] = v

        params_dict.update(kwargs)

        for k,v in params.items():
            if k not in params_dict.keys():
                params_dict[k] = v.default

        key = tuple(sorted(params_dict.items()))

        if key not in local_cache:
            local_cache[key] = fn(*args, **kwargs)
        return key, local_cache[key]
    return wrapper
@new_cache
def add(x,y=5):
    time.sleep(3)
    return x + y

print(add(2,5))
print('~~~~~~~~~~~~')
print(add(2,y=5))
print('~~~~~~~~~~~~')
print(add(2))
print('~~~~~~~~~~~~')
print(add(x=2, y=5))
print('~~~~~~~~~~~~')
print(add(y=5, x=2))
