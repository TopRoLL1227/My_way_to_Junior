# У Python декоратор @property використовується для створення властивостей класу. Властивість - це спеціальний вид атрибуту класу, 
# який дозволяє виконувати код при звертанні до атрибуту, таким чином, що він виглядає як звичайне значення атрибуту, 
# але може відповідати на певні дії (наприклад, отримання, встановлення, видалення).
# Декоратор @property дозволяє визначити метод як властивість, що дозволяє отримувати значення через звернення до нього як до атрибуту, без виклику методу.

class Person:
    def __init__(self, name, old):
        self.__name = name  # Щоб звертатися до закритих даних потрібні сеттери та геттери
        self.__old = old

    def get_old(self):     # Створюю getter 
        return self.__old
    
    def set_old(self, old):
        self.__old = old   # Створюю setter


p = Person('Jack', 20)
p.set_old(30)
print(p.__dict__)  # {'_Person__name': 'Jack', '_Person__old': 30}
print(p.get_old())  # 30

###########################################################################

class Person:
    def __init__(self, name, old):
        self.__name = name  # Щоб звертатися до закритих даних потрібні сеттери та геттери
        self.__old = old

    def get_old(self):     # Створюю getter 
        return self.__old
    
    def set_old(self, old):
        self.__old = old   # Створюю setter

    old = property(get_old, set_old)  # Створюється новий атрибут old який є об'єктом класу property. При створенні екземпляру цього класа йому передається 
                                      # посилання на gettar(get_old), а другим параметром посилання на setter (set_old)
                                      
                                      # Що відбувається? З кожного екземпляра класа можна без зайвих проблем посилатися до атрубутів old, класа Person.
                                      # Цей атрибут є об'єктом Property. При зверненні до old, наприклад: a = p.old, то автоматично буде викликаний
                                      # геттер(get_old).


p = Person('Jack', 20)
a = p.old

p.old = 35
print(p.old)  # 35
print(p.__dict__)  # {'_Person__name': 'Jack', '_Person__old': 35}

##########################################################################################################3
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Навіщо звертатися до властивостей якщо можна викликати метод напряму?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Як звертатися до атрибутів класу виключно через властивості? За допомогою декоратора property.<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#getter
#setter
#deletter

class Person1:
    def __init__(self, name, old):
        self.__name = name  # Щоб звертатися до закритих даних потрібні сеттери та геттери
        self.__old = old

    def get_old(self):     # Створюю getter 
        return self.__old
    
    def set_old(self, old):
        self.__old = old   # Створюю setter

    old = property() 
    old = old.setter(set_old)  # Можна використовувати ці декоратори, щоб метод класу відразу перетворити в об'єкт властивості класу Preporty
    old - old.getter(get_old)