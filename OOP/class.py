class Car:
    pass

a = Car()                  # змінна 'a' є об'єктом класу Car
print(a)                   # <__main__.Car object at 0x7faf5df57910>
print(type(a))             # <class '__main__.Car'>
print(isinstance(a, Car))  # True

b = Car()                  
print(b)                   # <__main__.Car object at 0x7f117315ad40>


class Car:
    model = 'BMW'
    engine = 2.0

c = Car()
print(c)