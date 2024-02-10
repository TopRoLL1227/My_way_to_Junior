class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

b = BankAccount('Misha', 1000)
print(b.balance)  # 1000
print(b.balance + 400)  # 1400

######################################

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, a):
        print('Method __add__ called')
        if isinstance(a, (BankAccount)):
            return self.balance + a.balance
        if isinstance(a, (int, float)):
            return self.balance + a
        raise NotImplemented
        
s = BankAccount('Simon', 100)
print(s + 55.5)  # Method __add__ called
               # 155.5

t = BankAccount('Tanya', 200)
print(t + s)  # 300