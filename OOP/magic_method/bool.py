# Любе значення в Python є об'єктом. Любий об'єкт має властивість правди.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('Call __len__')
        return abs(self.x - self.y)


p1 = Point(1, 2)
print(bool(p1))  # True


p2 = Point(3, 4)
print(bool(p2))  # True

print(bool(Point(5, 6)))  # True

print(bool(Point(7, 7)))  # False

# Якщо метод bool не реалізований, то Python буде дивитися на метод len. В інших випадках bool завжди буде правдивим. (Видали метод __len__ й запусти код)

#################################################################################################################################

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('Call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('Call __bool__')
        return self.x != 0 or self.y != 0
    
p1 = Point(1, 2)
print(bool(p1))  # True

p2 = Point(0, 0)
print(bool(p2))  # False  # не виконується жодна з умов