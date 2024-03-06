class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('getter')
        return self.__balance
    
    def set_balance(self, value):
        print('setter')
        if not isinstance(value, (int, float)):
            raise ValueError('Balance must be integer ')
        self.__balance = value

    balance = property(fget=get_balance, fset=set_balance)


# a = BankAccount('Ivan', 100)
# print(a.name)

# b = BankAccount('Masha', 200)
# b.get_balance()
# print(b.get_balance())
# b.set_balance(250)
# print(b.get_balance())

c = BankAccount('Grisha', 300)
# print(c.balance)
c.balance = 350