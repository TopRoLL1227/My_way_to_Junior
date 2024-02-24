# # super(). - У Python ключове слово super() використовується для доступу до методів батьківського класу з методів дочірнього класу. 
# Це дозволяє уникнути дублювання коду та забезпечити більшу гнучкість при розширенні функціональності класів.

# class Person:

#     def __init__(self, name, surname):
#         self.name = name
#         self.surnname = surname


#     def breathe(self):
#         print('people can breathe')

    
# class Doctor(Person):

#     def __init__(self, name, surname, age):
#         super().__init__(name, surname)
#         self.age = age


#     def breathe(self):
#         print('doctor can breathe')
#         super().breathe()


# p = Person('Taras', 'Shevchenko')
# d = Doctor('Stealh', ' Hummer', 30)

# d.breathe()  # doctor can breathe
#              # people can breathe

# print(p.name, p.surnname)
# print(d.name, d.surnname, d.age)


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2, fill=None):
        print(f'initilizator Geom for {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = fill


class Line(Geom):

     def draw(self):
        print('Paint')
        

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        #Geom.__init__(self, x1, y1, x2, y2)
        print(f'initilizator Rect')
        self.fill = fill


    def draw(self):
        print('Paint rect')


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
print(r.__dict__)  # {'x1': 1, 'y1': 2, 'x2': 3, 'y2': 4, 'fill': None}
