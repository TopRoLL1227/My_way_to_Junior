# Атрибути класу

class Person:
    name = 'Ivan'  # Атрибути
    age = 30  # Атрибути


print(Person())  # Результат виклику повертає екземпляр класу!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(Person())  # <__main__.Person object at 0x7fa9999578b0>
print(Person.name)  # Ivan # За допомогою символа "." можна звертатися до атрибутів класу та получати його значення.
print(Person.age)

# Як подивитися всі атрибути які існують в класі?
print(Person.__dict__)  # {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, 
                        #  '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


# Як змінити значення атрибуту?
Person.name = 'Vovik'
print(Person.name)  # Vovik

# Що буде, якщо вказати значення атрибуту якого не існує?
Person.x = 100
print(Person.x)  # 100 # Динамічно створився атрибут
print(Person.__dict__)  # {'__module__': '__main__', 'name': 'Vovik', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, 
                        # '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, 'x': 100}
Person.x = [1, 2, 3] # Знову динамічно створюється атрибут
print(Person.x)  # [1, 2, 3]

# Значення атрибутів можна встановити за допомогою вбудованої функції set. Також за її допомогою можна створити новий атрибут класа.
setattr(Person, 'x', 200)
print(Person.x)  # 200 # Зиінив атрибут .x зі списку [1, 2, 3] у ціле число 200

setattr(Person, 'y', 500)
print(Person.y)  # 500 # Створив новий атрибут зі значенням 500.

# Як видалити атрибути?
print(Person.__dict__)  # {'__module__': '__main__', 'name': 'Vovik', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, 
                        # '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, 'x': 200, 'y': 500}
del Person.x
print(Person.__dict__)  # {'__module__': '__main__', 'name': 'Vovik', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, 
                        # '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, 'y': 500}


#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Як значення атрибутів класу позначаються на екземплярах класа?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

class Person1:
    name1 = 'Ivan'
    age1 = 30

print(Person1())  # <__main__.Person1 object at 0x7fcd5415a830> # Результат виклику повертає екземпляр класу
a = Person1()  # Екземпляр класу збережений у змінній 'a'
               # В ньому автоматично зберігаються два атрибути, name1 й age1
print(a)          # <__main__.Person1 object at 0x7fcd5415a830>

b = Person1()
print(b)          # <__main__.Person1 object at 0x7fcd5415aa10> відрізняється від оригіналу та змінної 'a'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Person1.z = 700  #!!!!!!!!!!!!!!!!!!!!!!!!В такому випадку, змінним 'a' і 'b' було автоматично додано атрибут 'z' класу Person1!!!!!!!!!!!!!!!!