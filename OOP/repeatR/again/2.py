class Car:
    model = 'BMW'
    engine = 1.6


print(Car())


a1 = Car()
a2 = Car()

print(Car.__dict__)
print(a1.model)
print(a2.engine)

a1.seat = 4

print(a1.__dict__)
print(a1.seat)

print(a2.__dict__)
print(Car.__dict__)

a1.model = 'AUDi'
print(a1.model)

a2.size = 80

print(a2.size)
print(a2.__dict__)