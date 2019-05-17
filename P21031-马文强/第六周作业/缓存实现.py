from functools import wraps
import inspect
import time
def new_cache(fn):
    local_cache = {}
    @wraps(fn) # wraps(fn) -> partial(update_wrapper,wrapped=add(���̶�����))
    # weapper = partial(update_wrapper,wrapper) ->update_wrapper(wrapper)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn) #ǩ��Ԫ��
        params = sig.parameters #�б� �����ֵ�-> k-v��ɵĶ�Ԫ��
        params_dict = {}

        params_dict.update(zip(params.keys(),args)) #����λ�ô���
        params_dict.update(kwargs)  #���¹ؼ��ִ���
        for k,v in params.items():
            if k not in params_dict:
                params_dict[k] = v.default #����ȱʡֵ
        key = tuple(sorted(params_dict.items())) #��Ԫ���һ�£����򷵻ص���һ�����б�

        if key not in local_cache.keys():
            local_cache[key] = fn(*args, **kwargs) #���㱻��װ������ֵ
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
