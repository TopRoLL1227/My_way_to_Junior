class DepartamentIT:

    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    
    def info1(DepartamentIT):
        print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    @property
    def info2(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info3(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info4():
        print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    def hiring_pyt_def(self):
        self.PYTHON_DEV += 1

    
it1 = DepartamentIT()
print(it1.PYTHON_DEV)
it1.hiring_pyt_def()
print(it1.PYTHON_DEV)
it1.hiring_pyt_def()
print(it1.PYTHON_DEV)

print(DepartamentIT.PYTHON_DEV)