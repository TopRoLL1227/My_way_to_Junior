# Singleton
class Cat:

    __shared_attr = {
        'breed': 'pers',
        'colour': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


d = Cat()
g = Cat()

print(d.__dict__)
print(g.__dict__)

d.breed = 'siam'

print(d.breed)
print(g.breed)

d.name = 'Bob'
print(d.__dict__)
print(g.__dict__)

h = Cat()
