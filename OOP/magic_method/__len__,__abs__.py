class Point:
    def __init__(self, *args):
        self.__cords = args

    def __len__(self):
        return len(self.__cords)
    
    def __abs__(self):
        return list(map(abs, self.__cords))
    

    
asd = Point(1, 2, -5)

print(len(asd))  # 2
print(abs(asd))  # [1]

