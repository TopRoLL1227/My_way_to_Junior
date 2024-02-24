#  Slots Property Inheritance

class Rectangle:

    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value



r = Rectangle(3, 4)
#print(r.width)
print(r._Rectangle__width)

#################################3
# Inheritance

class Square(Rectangle):
    pass


s = Square(1, 2)

print(s.__dict__)
s.q = 100  # {}
print(s.__dict__)  # {'q': 100}

############################################################
class Square1(Rectangle):
    
    __slots__ = 'color'  # Він розширює slots батьківського класа!!!!!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color


d = Square1(1, 2, ' balck')
print(d.width, d.height, d.color)
#print(d.__dict__)  # Error

