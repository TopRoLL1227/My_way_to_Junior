class Person:
    name = 'Ivan'
    age = 30


# print(Person.__dict__)

# print(getattr(Person, 'name', 100))

# Person.age = 20
# print(Person.age)#
# Person.x = 100
# print(Person.__dict__)

# setattr(Person, 'new', 'old')
# print(Person.__dict__)
# print(Person.new)  # old

# del Person.x
# #print(Person.x)  # AttributeError: type object 'Person' has no attribute 'x'
# delattr(Person, 'new')
# #print(setattr(Person, 'new'))  # TypeError: setattr expected 3 arguments, got 2


print(Person())

a = Person()
b = Person()

Person.x = 100
print(a.x)
print(b.x)
