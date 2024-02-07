# Декоратори @classmethod / @staticmethod

# @classmethod:
# Цей декоратор вказує на те, що метод класу приймає перший аргумент, який є посиланням на клас (зазвичай позначений як cls).
# @classmethod дозволяє використовувати метод для роботи з класом, а не з конкретними об'єктами класу.
# Часто використовується для створення альтернативних конструкторів або методів, які мають доступ до класових атрибутів.

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):                                 # cls це посилання на клас Vector, тобто може звертатися до атрибуів класу, 
        return cls.MIN_COORD <= arg <= cls.MAX_COORD        # але не може посилатися на локальні атрибути екземляра класа
    
    def __init__(self, x, y):  
        self.x = self.y = 0  # Цей рядок ініціалізує обидва атрибути x та y об'єкта класу Vector значенням 0. 
                             # Це робиться для того, щоб у випадку неправильних координат (які не відповідають умовам validate), 
                             # вони мали значення за замовчуванням.
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y
 
v = Vector(1, 2)
print(v.get_coord())
print(Vector.validate(5))


#@staticmethod:
# Цей декоратор вказує на те, що метод не потребує доступу до об'єктів класу або його екземплярів.
# @staticmethod використовується, коли функція або метод не пов'язаний з конкретним екземпляром класу і не потребує доступу до його атрибутів.

# Створюється незалежна функція яка є проголошеною всередині класа.

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):                                 
        return cls.MIN_COORD <= arg <= cls.MAX_COORD        
    
    def __init__(self, x, y):  
        self.x = self.y = 0 
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y
    
    @staticmethod
    def norm2(x, y):
        return x*x + y*y

 
v = Vector(1, 2)
print(v.norm2(5, 6))  # 
