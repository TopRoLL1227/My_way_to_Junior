class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.balance / other


b = BankAccount('Ivan', 900)
print(b + 1)
print(b.__add__(100))

print(b.__sub__(10))

r = BankAccount('Tanya', 2000)
print(r + b)
