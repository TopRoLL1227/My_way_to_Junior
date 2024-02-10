# Простір імен класа


class DepartamentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):  # 1 варіант 
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info2(self):  # 2 варіант
        print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    @property
    def info_prop(self):  # 3 варіант
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @staticmethod
    def info_static():
        return DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV 
        
    @classmethod
    def info_class(cls):
        return cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV

    def hiring_pyt_dev(self):
        self.PYTHON_DEV = self.PYTHON_DEV + 1  # оператор '=' не змінює PYTHON_DEV, а лише створює новий, локальний атрибут PYTHON_DEV в екземлярі класа it1
        # ВАЖЛИВО. Якщо необхідно змінити атрибут PYTHON_DEV то до нього потрібно звертатися DepatamentIT.PYTHON_DEV

it1 = DepartamentIT()
it1.info()  # 4 3 2
it1.info2()  # 4 3 2
it1.info_prop  # 4 3 2
print(it1.info_class())  # (4, 3, 2)
print(it1.info_static()) # (4, 3, 2)
print(it1.PYTHON_DEV)  # 4
it1.hiring_pyt_dev()
print(it1.PYTHON_DEV)  # 5
print(DepartamentIT.PYTHON_DEV)  # 4
 