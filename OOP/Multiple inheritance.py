# Multiple inheritance у Python - це механізм, що дозволяє класам успадковувати атрибути та методи від більше ніж одного батьківського класу. 
# Це означає, що клас може мати більше одного прямого батька.
# Method Resolution Order

class Doctor:

    def can_cure(self):
        print('I am a doctor, i can healthy')

    def can_build(self):
        print('I am a men, and i also can build')  


class Builder:
    
    def can_build(self):
        print('I am builder, i can build')


class Person(Builder, Doctor):
    pass


# d = Doctor()
# b = Builder()
# p = Person()

# p.can_build()

print(Person.__mro__)

print('#'* 70)

#########################################################################################################

class Doctor1:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('I`ve finished study')

    def can_build(self):
        print('I am a men, and i also can build')  


class Builder1:

    def __init__(self, rank):
        self.rank = rank
    
    def can_build(self):
        print('I am builder, i can build')

    def graduate(self):
        print('I am studying')


class Person1(Builder1, Doctor1):

    def __init__(self, rank, degree):
        self.rank = rank
        self.degree = degree

    def __str__(self):
        return f"Person {self.rank}, {self.degree}"
        


# d = Doctor()
# b = Builder()
p = Person1(5, 'Magister')

# p.can_build()
print(p)

#######################################################################

class Doctor1:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('I`ve finished study')

    def can_build(self):
        print('I am a men, and i also can build')  


class Builder1:

    def __init__(self, rank):
        self.rank = rank
    
    def can_build(self):
        print('I am builder, i can build')

    def graduate(self):
        print('I am studying')


class Person1(Builder1, Doctor1):

    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor1.__init__(self, degree)

    def __str__(self):
        return f"Person {self.rank}, {self.degree}"
        


# d = Doctor()
# b = Builder()
p = Person1(5, 'Magister')

# p.can_build()
print(p)

