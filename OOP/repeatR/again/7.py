class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def public_data(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 1000000, 'VR12345')
account1.public_data()
print(account1._BankAccount__balance)
# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)