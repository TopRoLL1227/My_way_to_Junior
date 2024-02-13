class Car:
    model = 'BMW'
    engine = '1,6'


Car.model = 'AUDI'
print(Car.model)

Car.engine = '3.0 biT'
print(Car.engine)

Car.x = 'Tesla'
print(Car.x)  # Tesla
print(getattr(Car, 'x'))  # Tesla
print(Car.__dict__)  

Car.x = 'TeslaModelX'
print(Car.x)  # TeslaModelX
print(getattr(Car, 'x'))  # TeslaModelX

setattr(Car, 'model', 'newmodel')
print(Car.model)

setattr(Car, 'engine', 'E60 m5 5.0 ATMO')
print(Car.engine)  # 
print(getattr(Car, 'engine'))  # E60 m5 5.0 ATMO

del Car.x
#print(Car.x)  # Error
delattr(Car, 'model')
#print(getattr(Car, 'model'))  # Error


print('#############################################')
############################################################

class Car1:
    model = 'BMW'
    engine = '1,6'

a = Car1()
b = Car1()

Car1.year = 2000
print(a.__dict__)  # {}
print(getattr(a, 'year'))  # green

Car1.color = 'green'
print(b.__dict__)  # {}
print(getattr(b, 'color'))  # green

a.x_drive = 'Yes'
print(a.__dict__)  # {'x_drive': 'Yes'}
print(getattr(a, 'x_drive'))  # yes

b.m57 = 'legend'
print(b.__dict__)  # {'m57': 'legend'}
print(b.m57)  # legend
b.model = 'Bently'

delattr(Car1, 'model')
#print(Car1.model)  # Error
print(b.model) # Bently