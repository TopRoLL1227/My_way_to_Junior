class Person:
    pass

class Doctor(Person):
    pass

class Architector(Doctor):
    pass


print(issubclass(Person, object))

print(dir(object))
print(dir(Person))