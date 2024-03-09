class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


# print('sadfgsreg'.__len__())
# print((-1).__abs__())

p1 = Person('Volodymyr', 'Velikyi')
print(len(p1))

class Vidrizok():

    def __init__(self, point1, point2):
        self.x = point1
        self.y = point2

    def __len__(self):
        return abs(self)
    
    def __abs__(self):
        return abs(self.y - self.x)
    

t = Vidrizok(10, 5)
print(abs(t))