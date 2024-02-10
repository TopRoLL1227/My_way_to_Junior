#  __getitem__ , __setitem__ и __delitem__. звернення по індексу до екземпляра

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)
    
v1 = Vector(5, 233,700, 49)
print(v1)

v2 = Vector(10, 20, 30, 40, 50, 60, 70 ,80, 90)
print(v2)
#print(v2[1])  # Error # класи не підтримують індексування


############################################################################################################


class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)
    
    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError("Index out of range")

    
v1 = Vector(5, 233,700, 49)
print(v1)

v2 = Vector(10, 20, 30, 40, 50, 60, 70 ,80, 90)
print(v2)
#print(v2[1])  # Error # класи не підтримують індексування, але __getitem__

v3 = Vector(895, 533, 96, 453)
print(v3[2])  # 96


###########################################################################################################

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)
    
    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError("Index out of range")
        
    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('list assignment index out of range')
    
v1 = Vector(5, 233,700, 49)
print(v1)

v2 = Vector(10, 20, 30, 40, 50, 60, 70 ,80, 90)
print(v2)
#print(v2[1])  # Error # класи не підтримують індексування, але __getitem__

v3 = Vector(895, 533, 96, 453)
print(v3[2])  # 96

v4 = Vector(2, 4, 6 ,8)
v4[0] = 40
print(v4)  # [40, 4, 6, 8]

