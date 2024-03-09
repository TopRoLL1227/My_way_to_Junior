class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance
    
    @my_balance.setter
    def my_balance(self, value):
        self.__balance = value

    # def delete_balance(self):
    #     del self.__balance
    

    #my_balance = property(my_balance)


b = BankAccount('Vova', 200)

print(b.my_balance)






