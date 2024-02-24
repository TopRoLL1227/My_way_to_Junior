# slots - обмежує атрибути, менше займає місця в пам'яті, операції здійснюються швидше

class Points:

    def __init__(self, x , y):
        self.x = x
        self.y = y


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x , y):
        self.x = x
        self.y = y


p2 = PointSlots(3, 4)
print(p2.x)
p2.y = 100
print(p2.y)

# p2.s = 50  # AttributeError: 'PointSlots' object has no attribute 's'

