# practise 

class Point:

    
    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'point of coordinates ({self.x},{self.y})')



p1 = Point(1, 2)
print(p1.__dict__)  # {'x': 1, 'y': 2}

p2 = Point(-3, -4)
print(p2.__dict__)  # {'x': -3, 'y': -4}

p3 = Point()
print(p3.__dict__)  # {'x': 0, 'y': 0}
p3.move_to(5, 6)
print(p3.__dict__)  # {'x': 5, 'y': 6}
p3.move_to(-90, 6)
print(p3.__dict__)  # {'x': -90, 'y': 6}

p4 = Point(10)
print(p4.y)
p4.move_to(20, 30)
print(p4.y)
p4.go_home()

p5 = Point()
p5.print_point()
