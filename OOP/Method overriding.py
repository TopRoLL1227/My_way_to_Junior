# Перевизначення методів

class Person:

    def __init__(self, name):
        print('init Person')
        self.name = name

    
    def breathe(self):
        print('People breath')

    def walk(self):
        print('People walk')


class Doctor(Person):
    
    def breathe(self):
        print('Doctor breath')

    def __str__(self):
        return f'Doctor {self.name}'    


d = Doctor("Adam")
p = Person("Back")

print(d, p)




