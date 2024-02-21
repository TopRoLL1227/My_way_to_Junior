class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        self.a * self.b


    def __eq__(self, other):
        print("__eq__ call")
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b
    
    def __lt__(self, other):
        print("__lt__ call")
        if isinstance(other, Rectangle):
            return self.a < other.a 
        elif isinstance(other, (int,float)):
            return self.area < other



a = Rectangle(1, 2)
b = Rectangle(3, 4)

print(a == b)