# Метод екземляра класа
# Метод екземпляра класу в Python - це метод, який пов'язаний з конкретним екземпляром класу. 
# У визначенні методу екземпляра ви не використовуєте декоратор @classmethod. 
# Зазвичай це метод, який взаємодіє з конкретними атрибутами та методами об'єкта, до якого він викликається.

class Car:
    model = 'BMW'
    engine = 1.6

    def drive(self):  # self введе на об'єкт 'a' через який був викликаний даний метод. Тобто це посилання на екземляр класу 'a'.
        print('Let\'s go ' + str(self))



a = Car()
print(a.drive)  # <bound method Car.drive of <__main__.Car object at 0x7f6518b3a8f0>>
a.drive()  # TypeError: Car.drive() takes 0 positional arguments but 1 was given
           # IMPORTANT: Якщо функції drive() передати параметр self то все запрацює!  # Let's go <__main__.Car object at 0x7f843951a8f0>

#Car.drive()  #
Car.drive(a)  # Let's go <__main__.Car object at 0x7f843951a8f0>


class Car1:
    model = 'BMW'
    engine = 1.6

    def drive1(self, x, y):
        self.x = x
        self.y = y

    def get_drive1(self):
        return (self.x, self.y)


exem = Car1()
exem.drive1(1, 2)

exem2 = Car1()
exem2.drive1(3, 4)

print(exem.__dict__)
print(exem.x)  # 1 
print(exem.y)  # 2

print(exem2.__dict__)
print(exem2.x, exem2.y)  # 3 4

exem3 = Car1()
exem3.drive1(10, 20)
print(exem3.__dict__)
print(exem3.get_drive1())


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>IMPORTANT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Коли створюється багато нових екземплярів одного й того ж класу тоді метод класу def drive1 не копіюється в окремі екземпляри, а лише за допомогою
# параметра self програма знає з яким екземляром класа в даний момент працює метод drive1  