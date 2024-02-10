#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>IMPORTANT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#У Python словники використовують хеш-функції для швидкого пошуку та доступу до значень за ключем. Коли ви додаєте об'єкт до словника, 
# Python обчислює хеш-значення ключа за допомогою функції hash(), а потім використовує це значення для визначення індексу в хеш-таблиці, 
# де зберігаються пари "ключ-значення". Якщо ви додаєте об'єкти з однаковим хешем до словника, то вони будуть поміщені 
# в одну й ту ж саму комірку хеш-таблиці, а потім Python буде використовувати метод порівняння об'єктів eq() для перевірки, чи рівний ключ,
# який ви додаєте, ключу, який вже є у словнику. Якщо два ключі мають однаковий хеш, але не є рівними (за методом eq()), то вони будуть зберігатися 
# в одній комірці хеш-таблиці, але будуть оброблятися як окремі ключі.
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

print(hash('Python'))  # -6221616492973848572
print(hash(123))       # 123
print(hash((1, 2, 3))) # 529344067295497451

print(hash('Python'))  # -6221616492973848572

#IMPORTANT!!!!>>>>>>>>>>> Для однакових об'єктів hash однаковий, але зворотнє твердження невірно!!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Якщо хеш однаковий то це не означає, що об'єкти теж однакові. Вони можуть бути різними. Однак, якщо хеш нерівний то й об'єкти точно нерівні.
# Хеши можна вираховувати лише для незмінних об'єктів.

# Деякі об'єкти, такі як словарі, використовують hash в якості ключів. Коли прописується ключ у dict, він повинен відноситися до незмінюваого об'єкту.
# Приклад:
d = {} # dict зберігає ключі у формі "хеш ключа, ключ"
d[5] = 3
d['python'] = '123'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(1, 2)

# З точки зору функції hash ці об'єкти різні
print(hash(p1))  # 8737233262211
print(hash(p2))  # 8737233262292
# А як він розуміє, що ці об'єкти різні?
print(p1 == p2)  # False # Звідси об'єктиу hash різні

# Але:

class Point1:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # грубо кажучи, я заставляю свою програму думати, що x та y це одне й теж саме, відповідно хеш у них однаковий.
        return self.x == other.x and self.y == other.y


p1 = Point1(1, 2)
p2 = Point1(1, 2)

print(p1 == p2)  # True
#print(hash(p1))  # TypeError: unhashable type: 'Point1'
#print(hash(p2))  # TypeError: unhashable type: 'Point2'

# Але:

class Point2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # грубо кажучи, я заставляю свою програму думати, що x та y це одне й теж саме, відповідно хеш у них однаковий.
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point2(1, 2)
p2 = Point2(1, 2)

print(hash(p1))  # -3550055125485641917
print(hash(p2))  # -3550055125485641917

d = {}
d[p1] = 1
d[p2] = 2
print(d)  # {<__main__.Point2 object at 0x7fbe98f93df0>: 2}