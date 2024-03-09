class Person:  # parent

    def can_breath(self):
        print('I can breath')

    def can_walk(self):
        print('I can walk')


class Doctor(Person):  # subclass

    def can_cure(self):

        print('I can health')

class Ortoped(Doctor):
    pass


class Architector:

    def can_build(self):
        print('I can build ')


d = Doctor()
d.can_breath()
d.can_walk()
o = Doctor()
o.can_breath()
o.can_cure()

print(issubclass(Doctor, Person))