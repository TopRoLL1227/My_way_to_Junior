# У Python декоратор @property використовується для створення властивостей класу. Властивість - це спеціальний вид атрибуту класу, 
# який дозволяє виконувати код при звертанні до атрибуту, таким чином, що він виглядає як звичайне значення атрибуту, 
# але може відповідати на певні дії (наприклад, отримання, встановлення, видалення).
# Декоратор @property дозволяє визначити метод як властивість, що дозволяє отримувати значення через звернення до нього як до атрибуту, без виклику методу.

# getter та setter прописуються для кожного приватного атрибуту

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property  # Обов'язково перед геттером!!! Тепер цей гетор є об'єктом властивості для зчитування приватного атрибута (__old)
    def get_old(self):
        return self.__old
    
    def set_old(self, a):
        self.__old = a
        print(self.__old)

    old = property(get_old, set_old)  # Створюється новий атрибут old який є об'єктом класу property. При створенні екземпляру цього класа йому передається 
                                      # посилання на getter(get_old), а другим параметром посилання на setter (set_old)
    
                                      # Що відбувається? З кожного екземпляра класа можна без зайвих проблем посилатися до атрубутів old, класа Person.
                                      # Цей атрибут є об'єктом Property. При зверненні до old, наприклад: a = p.old, то автоматично буде викликаний
                                      # геттер(get_old). При записуванні даних, автоматично запускається сеттер! Тобто, за допомогою атрибута old 
                                      # можна зчитувати чи записувати дані.
    asd = property()
    asd = asd.setter(set_old)  # створені за допомогою декоратора
    asd = asd.getter(get_old)  # вони потрібні для того, щоб метод класу відразу перетворити в об'єкт властивості класу Preporty



p = Person('Sanya', 25)
#print(p.get_old())  # 25
print(p.get_old)  # Тепер, за допомогою @property можна зчитати напряму інформацію з геттера, але записати ні.
p.set_old(26)  # 26
#print(p.get_old())  # 26

#a = p.old
#print(a)  # 26 ###  викликається геттер

p.old = 30  # 30 ### викликається сеттер
# Щоб розробник не запам'ятовував назву кожного приватного атрибуту, створено декоратор (об'єкт) #property


##############################################################################################################################
# Декоратори - getter, setter, deleter

