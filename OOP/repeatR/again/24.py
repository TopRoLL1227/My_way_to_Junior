class Person:

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breath(self):
        print('Men breath')

    def walt(self):
        print('Men walk')


class Doctor(Person):

    name = 'ivan'
    
    def breath(self):
        print('Doctor breath')

    def __str__(self):
        return f'Doctor {self.name}'


d = Doctor('John')
p = Person('Adam')

print(d.name)
print(p.name)

print(p)
print(d)

