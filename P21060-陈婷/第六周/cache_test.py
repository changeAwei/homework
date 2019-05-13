import inspect
import time
from functools import wraps
def get_cache(fn):
    key_dict = {}
   # @wraps(fn)
    def _getcache( *args,  **kwargs):
        parame_dict ={}
        sigs = inspect.signature(fn)
        parame = sigs.parameters

        for k, v in parame.items():
            parame_dict[k] = v.default
        parame_dict.update(zip(parame.keys(), args))
        parame_dict.update(kwargs)

        key = tuple(sorted(parame_dict.items()))
        print(key)
        #key_dict.setdefault(key,fn(*args,**kwargs))   #
        if key not in key_dict:
            key_dict[key] = fn (*args,**kwargs)
        return key_dict[key]
    return _getcache

@get_cache
def add(x=4,y=5):
    time.sleep(3)
    return x + y
add()
print('*'*30)
add(4,6)

print('*'*30)
add(x=4,y=6)
print('*'*30)
add(4,y=6)

