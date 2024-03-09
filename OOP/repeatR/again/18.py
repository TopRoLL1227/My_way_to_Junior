class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(id(p1))
print(id(p2))

print(p1 == p2)

d = {}
d[1] = 900
print(d)
d[[3, 4]]



