# 使用已学习的装饰器相关知识自己实现functools.lur_cache。
from functools import wraps
import datetime
import inspect
def lx_cache(duration=5):
    def _lx_cache(fn):
        local_cache = {}  # 对不同名函数是不同的cache
        @wraps(fn)
        def wrapper(*args, **kwargs):
            def clear_expire():
                expire_keys = []
                for k, (_, stamp) in local_cache.items():
                    if datetime.datetime.now().timestamp() - stamp > duration:
                        expire_keys.append(k)
                for k in expire_keys:
                    local_cache.pop(k)
            def _make_key(args, kwargs):
                sig = inspect.signature(fn)
                params = sig.parameters
                params_dict = {}
                # 接收参数
                params_dict.update(zip(params.keys(), args))
                params_dict.update(kwargs)
                # 缺省值
                for k, v in params.items():
                    if k not in params_dict:
                        params_dict[k] = v.default
                key = tuple(sorted(params_dict.items()))
                return key

            clear_expire()#清理缓存
            key = _make_key(args, kwargs)

            if key not in local_cache.keys():#进行判断
                local_cache[key] = fn(*args, **kwargs), datetime.datetime.now().timestamp()
            return local_cache[key]
        return wrapper
    return _lx_cache
@lx_cache()
def add(x=4, y=5):
    return x + y
