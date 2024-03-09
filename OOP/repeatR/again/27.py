class Doctor:

    def can_cure(self):
        print('I am a doctor, i can healty')

    def can_build(self):
        print('I am a doctor, i can build')


class Builder:

    def can_build(self):
        print('I am a buidler, i can build')

class Person(Doctor, Builder):
    
    def can_build(self):
        print('I am a men, i also can build')


s = Person()
s.can_build()

print(Person.__mro__)
