class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks


    def __getitem__(self, item):
        return self.surname[item]
    

    def __iter__(self):
        print('call iter')
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


Vlad = Student('Vlad', 'Ivanivich', [5, 5, 4, 5])
for i in Vlad:
    print(i)







# b = [3, 4, 5, 6]
# s = iter(b)
# print(next(s))
# print(next(s))
# print(next(s))
# print(s.__next__())
