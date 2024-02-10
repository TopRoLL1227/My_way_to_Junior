# Поліморфизм - це можливість оброблення різних об'єктів шляхом використання одного й того ж самого методу по назві

from polymorphism import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

# print(rect1.get_rect_area())
# print(rect2.get_rect_area())

sq1 = Square(5)
sq2 = Square(7)

# print(sq1.get_square_area())
# print(sq2.get_square_area())

cir1 = Circle(5)
cir2 = Circle(7)
# print(cir1.get_circle_area())
# print(cir2.get_circle_area())


# figures = [rect1, rect2, sq1, sq2, cir1, cir2]
# for i in figures:
#     if isinstance(i, Square):
#         print(i.get_square_area())
#     elif isinstance(i, Circle):
#         print(i.get_circle_area())
#     else:
#         print(i.get_rect_area())

f1gures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figures in f1gures:
    print(figures, figures.get_area())