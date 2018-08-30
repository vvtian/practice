#用装饰器显示该函数的执行时长
import time
import datetime
from functools import wraps

def timeit(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start=datetime.datetime.now()
        ret=fn(*args,**kwargs)
        delta=(datetime.datetime.now()-start).total_seconds()
        print('{} took {} s'.format(fn.__name__,delta))
        return ret
    return wrapper

@timeit
def add(x, y):
    time.sleep(2)
    return x + y

print(add(2,3))

#使用上下文管理显示该函数的执行时长
def add(x, y):
    time.sleep(2)
    return x + y

class TimeIt2:
    def __init__(self,fn):
        self.fn=fn

    def __enter__(self):
        self.start=datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delta=(datetime.datetime.now()-self.start).total_seconds()
        print('*****{} took {} s'.format(self.fn.__name__,self.delta))

    def __call__(self,x,y):
        print('*****',x,y)
        return self.fn(x,y)


with TimeIt2(add) as f:
    f(2,3)
