class Person:

    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def __len__(self):
        return len(self.name + self.surname)
    
    def __abs__(self):
        return abs(self.number)


a = Person('123123', 'asdfasdf', -84)
print(len(a))  # 14
print(abs(a))  # 84

class Vidrizok:

    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return self.x2 - self.x1
    
    # def __len__(self):
        # return abs( self)
    
    def __abs__(self):
        return abs(self.x1 - self.x2)
    
t = Vidrizok(5, 9)
print(len(t))

print(abs(t))