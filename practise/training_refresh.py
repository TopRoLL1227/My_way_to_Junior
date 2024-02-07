class One:
    def __init__(self, x, z, y):
        self.x = x
        self.z = z
        self.y = y
    
    @classmethod
    def two(cls, a):
        return cls(*a.split(','))
    
asd = One.two("1,2,3")
print(asd.x, asd.z, asd.y)



s = '5,6,7'
print(*s)
