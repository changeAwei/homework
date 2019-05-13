from functools import wraps
import inspect
import time

def Myself_cache(fn):
    Mydict = {} #用于记录函数计算结果
    @wraps(fn)
    def wrapper(*args,**kwargs):
        tmpsig = inspect.signature(fn)  # x,y的元组
        tmpparam = tmpsig.parameters #x,y写入顺序,有序字典
        tmpdict = {}  #临时字典,用于记录参数
        tmpdict.update(zip(tmpparam.keys(),args)) # 位置传参写入
        tmpdict.update(kwargs)#关键字参数写入
        for k,v in tmpparam.items():
            if k not in tmpdict:
                tmpdict[k] = v.default #缺省值写入
        key = tuple(sorted(tmpdict.items())) #dict中key是可hash的,tuple包一下
        if key not in Mydict.keys():
            Mydict[key] = fn(*args,**kwargs)
        return Mydict[key]
    return wrapper

@Myself_cache
def add(x,y=3):
    time.sleep(5)#测试是否记录缓存
    return x+y


