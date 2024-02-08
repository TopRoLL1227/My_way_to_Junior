class Square:
    def __init__(self, a):
        self.side = a
        self.__area = None

    @property 
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side ** 2
        return self.side
    

asd = Square(6)
#print(asd.area())  # Звернення до area як до функції

print(asd.area) # 36  # звернення до area як до властивості
asd.side = 7

print(asd.area)  # 49

print(asd.area)