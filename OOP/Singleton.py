# Моніторний об'єкт
# У паттерні проектування Singleton об'єкт класу має лише один екземпляр, 
# і цей екземпляр надає глобальний доступ до точки контролю для цього єдиного екземпляра

class Cat:
    breed = 'pers'

a = Cat()
b = Cat()
a.breed = 'siam'
print(a.__dict__)  # {'breed': 'siam'}
print(b.__dict__)  # {}
print(a.breed)     # siam
print(b.breed)     # pers
c = Cat()
c.color = 'blue'
print(c.color)     # blue

# Як зробити так, щоб при зміні одого атрибута це впливало на всі інші екземляри класа


class Cat1:
    __shared_attr = {         # змінний атрибут
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat1.__shared_attr


d = Cat1()
g = Cat1()

print(d.__dict__)  # {'breed': 'pers', 'color': 'black'}
print(g.__dict__)  # {'breed': 'pers', 'color': 'black'}


d.breed = 'siam'
print(d.__dict__)  # {'breed': 'siam', 'color': 'black'}
print(g.__dict__)  # {'breed': 'siam', 'color': 'black'}


d.name = 'Bobby'
print(d.__dict__)  # {'breed': 'siam', 'color': 'black', 'name': 'Bobby'}
print(g.__dict__)  # {'breed': 'siam', 'color': 'black', 'name': 'Bobby'}