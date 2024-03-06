class Cat:
    __shared_attr_ = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr_

a = Cat()
print(a.breed)

a.color = 'black'
print(a.color)

d = Cat()
g = Cat()
print(d.__dict__)
print(g.__dict__)

d.breed = 'siam'
print(d.__dict__)
print(g.__dict__)


class Car:
    __shared__attr2_ = {
        'model': 'AUDI',
        'engine': 2.0
    }

    def __init__(self):
        self.__dict__ = Car.__shared__attr2_

asd = Car()
zxc = Car()
print(asd.__dict__)
asd.engine = 3.0
print(asd.engine)
print(zxc.engine)