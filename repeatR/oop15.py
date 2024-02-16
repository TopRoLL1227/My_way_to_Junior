class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
    

rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)
#print(rect1.get_rect_area(), rect2.get_rect_area())


class Square:

    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a **2
    
sq1 = Square(2)
sq2 = Square(4)
#print(sq1.get_square_area(), sq2.get_square_area())


class Circle:

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2

 
cr1 = Circle(5)
cr2 = Circle(10)

#print(cr1.get_circle_area(), cr2.get_circle_area())



figures = [rect1, rect2, sq1, sq2, cr1, cr2]
for figure in figures:
    print(figure.get_area())
    # if isinstance(figure, Square):
    #     print(figure.get_square_area())
    # elif isinstance(figure, Rectangle):
    #     print(figure.get_rect_area())
    # else:
    #     print(figure.get_circle_area())




