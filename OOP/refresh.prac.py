from refresh import Rectangle, Square, Circle

pr1 = Rectangle(2, 4)

sq1 = Square(5)

cr1 = Circle(7)

figures = [pr1, sq1, cr1]
for figure in figures:
    print(figure.get_area())