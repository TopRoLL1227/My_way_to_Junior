class Vovik:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __mul__(self, a):
        if isinstance(a, Vovik):
            return self.balance + a.balance
        if isinstance(a, (int, float)):
            return self.balance + a
        

vovik = Vovik('Vovik', 1000)
print(vovik * 2)


###

class Repeat:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, b):
        if isinstance(b, Repeat):
            return self.balance + b.balance
        if isinstance(b, (int,float)):
            return self.balance + b
        
m = Repeat('Masha', 1000)
print(m + 100)

i = Repeat('Ivan', 500)
print(m + i)