class Batya:

    def walk(self):
        print('i can walk')

class Doctor(Batya):

    def can_health(self):
        print('i can healt')

class Architector(Batya):

    def can_build(self):
        print('i can build')


d = Doctor()
a = Architector()

d.can_health()
a.can_build()

a.walk()

print(issubclass(Batya, Doctor))


