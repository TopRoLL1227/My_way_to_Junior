class DepartamentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def first_round(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def second_round(self):
        print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    @property
    def third_round(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def fourth_round(cls):
        return cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV
    
    @staticmethod
    def fifth_found():
        return DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV
    
    def bulba(self):
        self.GO_DEV = self.GO_DEV
    


asd = DepartamentIT()
asd.first_round()
asd.second_round()
asd.third_round
print(asd.fourth_round())
print(asd.fifth_found())

print(DepartamentIT.GO_DEV)
asd.bulba = 5
print(asd.bulba)

