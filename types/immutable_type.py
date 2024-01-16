#  Кортежі (tuple):
my_tuple = (1, 2, 3)
# Неможливо змінити значення, додати чи видалити елемент


#  Рядки (str):
my_string = "Hello"
#  Неможливо змінити символи рядка


#  Не змінні множини (frozenset):
my_frozenset = frozenset({1, 2, 3})
# Неможливо додати або видалити елементи після створення


#  Логічні значення (bool):
my_bool = True
#  Неможливо змінити значення булевого типу


#  Числові типи:
#  int, float, complex: Ці числові типи даних є немутабельними. Наприклад:
my_int = 42
#  Неможливо змінити значення my_int після створення


#  Замовчування (NoneType):
#  Тип NoneType, представлений значенням None, є немутабельним.
my_none = None
#  Неможливо змінити значення my_none після створення


#  Enumerations (enum.Enum):
#  Тип даних, представлений класом перерахування (enum), також є немутабельним.
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
#  Неможливо змінити значення перерахувань після створення


# Слайди (slice):
# Тип даних, який використовується для створення зрізів послідовностей, також є немутабельним.
    my_slice = slice(0, 3)
# Неможливо змінити значення my_slice після створення


# Комплексні числа (complex):
# Комплексні числа є немутабельними, і їх частини (real та imag) не можна змінювати.
    my_complex = complex(1, 2)
# Неможливо змінити реальну чи уявну частину після створення

my_number = 10  # 139779296363024
other_number = 10  # 139779296363024

my_list = [1, 2, 3]  # 140595837457664
other_list = [1, 2, 3]  # 140595837459712

info = {
    'name': 'Vova',
    'is_student': True
}  
print(id(info))  # 140696444200000
info_copy = info
print(id(info_copy))  # 140696444200000
info['reviews_qty'] = 5
print(info)  # {'name': 'Vova', 'is_student': True, 'reviews_qty': 5}
print(id(info))  # 140696444200000

baza = {
    'name': 'Vova',
    'is_student': True
} 
info_baza = baza

print(id(baza))  # 140567442105152
print(id(info_baza))  # 140567442105152
info_baza1 = baza.copy()  # Часткова копія!!!!!!!!!!!!!!! Якщо є вкладені словарі то посилання на них зберігаються. 
# Для цього потрібно from copy import deepcopy.
print(id(info_baza1))  # 140567442542400
