# Використання функції в якості атрибута класу

class Car:
    model = 'BMW'
    engine = 1.6

    def drive():
        print('Let\'s go')

print(Car())
print(Car.__dict__)  # {'__module__': '__main__', 'model': 'BMW', 'engine': 1.6, 'drive': <function Car.drive at 0x7f570774a200>, 
                     # '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}

Car.drive()  # Let's go 
getattr(Car, 'drive')()  # Let's go !!!!!!!!!! Аналогічно попередньому виклику

a = Car()

print(a.__dict__)  # {}
print(a.drive)  # <bound method Car.drive of <__main__.Car object at 0x7f3c47756830>> ЗВЕРНГИ УВАГУ BOUND METHOD <<<<<<<<<<<<<<<<<<
                # Тобто для екземляру класу це метод, а для класу це функція
print(a.model)