#shape基类，要求所有子类都必须提供面积的计算，子类有三角形、矩形、圆。
#圆类的数据可序列化
import math
import json
import msgpack

class Shape:
    pass

class Tri(Shape):
    def __init__(self,bottom,heigh):
        self.bottom=bottom
        self.heigh=heigh

    @property                  #属性装饰器
    def cal(self):
        self.sq=0.5*self.bottom*self.heigh
        return self.sq

class Rec(Shape):
    def __init__(self, bottom, heigh):
        self.bottom = bottom
        self.heigh = heigh

    @property
    def cal(self):
        self.sq = self.bottom * self.heigh
        return self.sq

class Cir(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def cal(self):
        self.sq = math.pi*self.radius**2
        return self.sq

print(Tri(3,4).cal)

class Smixin:
    def dumps(self,t='json'):
        if t=='json':
            return json.dumps(self.__dict__)
        elif t=='msgpack':
            return msgpack.packb(self.__dict__)
        else:
            raise NotImplementedError

class Cirsimxin(Smixin,Cir):
    pass

xx=Cirsimxin(2)
print(xx.dumps('msgpack'))
