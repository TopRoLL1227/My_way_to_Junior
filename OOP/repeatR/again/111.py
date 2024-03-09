from p19 import Rectangle, Square

rect1 = Rectangle(1, 2)
rect2 = Rectangle(3, 4)

# print(rect1.get_rect_area(),
      # rect2.get_rect_area())

sq1 = Square(2)
sq2 = Square(4)

# print(sq1.get_square_area(),
#       sq2.get_square_area())

figures = [rect1, rect2, sq1, sq2]
for item in figures:
    print(item.get_area())