class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, value):
        print('setter')
        self.__side = value
        self.__area = None


    @property
    def area(self):
        if self.__area == None:
            print('calculate area')
            self.__area = self.side**2
        return self.__area
        
        
a = Square(5)
print(a.area)

a.side = 6
print(a.area)