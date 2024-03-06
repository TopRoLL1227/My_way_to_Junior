class Car:
    model = 'AUDI'
    engine = '2.0'

a6 = Car()
q7 = Car()

print(a6.__dict__)  # {}
print(q7.__dict__)  # {}

a6.seat = 4
q7.seat = 5

print(a6.__dict__)  # {'seat': 4} 
print(q7.__dict__)  # {'seat': 5}
#print(Car.__dict__)

print(getattr(a6, 'model'))  # Audi
setattr(a6, 'model', 'MERCEDES')
print(a6.model)              # Mercedes
print(a6.__dict__)           # {'seat': 4, 'model': 'MERCEDES'}
 