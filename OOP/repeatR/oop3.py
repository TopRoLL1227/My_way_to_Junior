# Функция як атрибут класса

class Car:
    model = 'TOYOTA'
    engine = 3.5

    def drive():
        print('Let\'s go')


Car.drive()
s = getattr(Car, 'drive')()

exem = Car()
print(exem.__dict__)  # {}

print(Car.drive)  # <function Car.drive at 0x7f85f8b6a200>  # ДЛЯ КЛАСУ ЦЕ ФУНКЦІЯ
print(exem.drive)  # <bound method Car.drive of <__main__.Car object at 0x7f0cbff56aa0>>  # ДЛЯ ЕКЗЕМПЛЯРУ КЛАСУ ЦЕ МЕТОД




class Vova:

    @staticmethod
    def sanya():
        print("We are bro's")


Vova.sanya()
bro = Vova()
print(bro.sanya)
bro.sanya()







