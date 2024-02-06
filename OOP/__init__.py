# Метод __init__ в Python є спеціальним методом, який викликається автоматично при створенні нового екземпляра класу. 
# Цей метод використовується для ініціалізації атрибутів об'єкта. Тобто, для заповнення об'єкта будь-якими значеннями.


class Cat:
    breed = 'pers'

    def set_value(self, value, age = 0):
        self.name = value
        self.age = age

    def __init__(self):  # Приймає екземляр який створюється в процесі виклику класу всередину цього методу. Метод __init__ приймає на вхід об'єкт.
        print(f"hello new object is {self}")
      

bob = Cat()  # hello new object is <__main__.Cat object at 0x7f8299b5aad0>
bob.set_value('Bob')
print(bob.__dict__)  # {'name': 'Bob', 'age': 0}
print(bob.name, bob.age)  # Bob 0


tom = Cat()  # hello new object is <__main__.Cat object at 0x7f8299b5aa10>

#####################################################################################################################

class Cat1:

    def __init__(self, name, breed, age, color):
        print(f'Hello my cat {name}, {breed}, {age} ,{color}')
    

Cat1('Boobik', 'siam', 10, 'gray')  # Hello my cat Boobik, siam, 10 ,gray

######################################################################################################################

class Cat2:

    def __init__(self, name, breed = 'siam', age = 5, color = 'gray'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


loompik = Cat2('Loompik')
print(loompik.name, loompik.breed, loompik.age, loompik.color)

energizer = Cat2('Energizer')
print(energizer.name, energizer.breed, energizer.age, energizer.color)
