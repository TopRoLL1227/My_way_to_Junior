# Наслідування в об'єктно-орієнтованому програмуванні. Важлива ієрархія.

class Doctor:

    def can_breath(self):
        print('I can breath')

    def can_walk(self):
        print('I can walk')

    def can_cure(self):
        print('I can healh')


class Architect:

    def can_breath(self):
        print('I can breah')

    def can_walk(self):
        print('I can walk')

    def can_build(self):
        print('I can build')
    

d = Doctor()
d.can_cure()
d.can_walk()


a = Architect()
a.can_build()
a.can_walk()

# a.can_cure()  # AttributeError: 'Architect' object has no attribute 'can_cure'
# >>>>>>>>>>>>>>>>>>>>>>>>>Щоб не копіювати код, можна застосувати принцип наслідування, реалізувавши в окремому класі<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

print('############################')

class Person:  # Батьківський клас # parent

    def can_breath(self):
        print('I can breath')

    def can_walk(self):
        print('I can walk')


class Doctor1(Person):  # subclass

    def can_cure(self):
        print('I can healh')


class Ortoped(Doctor1):
    pass


class Architect1(Person):  # subclass

    def can_build(self):
        print('I can build')



d = Doctor1()
d.can_cure()
d.can_walk()

a = Architect1()
a.can_build()
a.can_walk()

e = Ortoped()
e.can_breath()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
e.can_walk()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
e.can_cure()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

print(issubclass(Doctor1, Person))  # True
print(isinstance(d, Doctor1))  # True
print(isinstance(d, Person))  # True
print(issubclass(Ortoped, Doctor1))  # True<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print(issubclass(Ortoped, Person))  # True<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

