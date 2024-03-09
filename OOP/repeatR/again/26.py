class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name}, {self.surname}'
    
    def info(self):
        print('Parent class')
        print(self)


    def breathe(self):
        print('Men breathe')


class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name}, {self.surname}'
    
    def breathe(self):
        super().breathe()
        print('Doctor breathe')
        super().breathe()


p = Person('Taras', 'Volodymyrovuch')
d = Doctor('Leonid', 'Vasylovich', 40)

print(p.name, p.surname)
print(d.name, d.surname, d.age)
d.info()