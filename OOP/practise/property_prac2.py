def BMI(h, w):
    if isinstance(h, float) and isinstance(w, int):
        return w / (h**2) 
    elif isinstance(h, int) and isinstance(w, int):
        return w / ((h / 100)**2)
    else:
        raise ValueError('Try again')


class My_first_big_class:
    def __init__(self, height, weight, age):
        self.__height = height
        self.__weight = weight
        self.__age = age

    # метод для отримання значення height
    def get_height(self):
        return self.__height
    
    # метод для отримання значення weight
    def get_weight(self):
        return self.__weight
    
    # метод для отримання значення age
    def get_age(self):
        return self.__age
    
    # метод для встановлення значення height
    def set_height(self, a):
        self.__height = a
        print(self.__height)

    # метод для встановлення значення weight
    def set_weight(self, b):
        self.__weight = b
        print(self.__weight) 

    # метод для встановлення значення age
    def set_age(self, c):
        self.__age = c
        print(self.__age)

    # використання декоратора для створення властивостей
    imt_height = property(get_height, set_weight)
    imt_weight = property(get_weight, set_weight)
    imt_age = property(get_age, set_age)


bmi = My_first_big_class(180, 80, 30)
print(bmi.imt_height)
bmi.imt_height = 190




