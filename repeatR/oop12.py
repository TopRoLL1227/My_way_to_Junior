class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def go1(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def go2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    @property
    def go3(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @staticmethod
    def go4():
        return DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV
    
    @classmethod
    def go5(cls):
        return cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV
    
    def add(self):
        self.GO_DEV = self.GO_DEV + 10

s = DepartmentIT()

s.go1()
s.go2()
s.go3
print(s.go4())
print(s.go5())
s.add()

print(s.GO_DEV)
DepartmentIT.add(s)
print(DepartmentIT.GO_DEV)



