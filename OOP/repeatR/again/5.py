class Point:

    def __init__(self, x=0, y=0):
        self.move_to(x, y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"Point on coord {self.x}, {self.y}")

    def calc_distance(self, anoither_point):
        if isinstance(anoither_point, Point):
            raise ValueError("Arg must be class: 'Point'" )






p1 = Point(3, 4)
p2 = Point(-54, 32)

p3 = Point()
p3.move_to(3, 4)
print(p3.__dict__)

p4 = Point(4)
p4.move_to(7, 8)
print(p4.__dict__)

p5 = Point(10, 20)
p5.print_point()

