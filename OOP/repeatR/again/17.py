class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        self.a + self.b

    def __eq__(self, other):
        print("__eq__ call")
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b
        
    def __lt__(self, other):
        print("__lt__ call")
        if isinstance(other, Rectangle):
            return self.area < other.area 


v = Rectangle(1, 2)
r = Rectangle(1, 2)

print(v == r)

print(id(v))
print(id(r))