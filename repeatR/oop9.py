class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance


    def get_balance(self):
        return self.__balance
    

    def set_balance(self, value):
        if isinstance(value, (int, float)):
            self.__balance = value
        else:
            raise ValueError('Number must be str')
        
    def delete_balance(self):
        print('delete balance')
        del self.__balance


    my_balance = property(get_balance)
    #my_balance = my_balance.setter(set_balance)
    #my_balance = my_balance.deleter(delete_balance)

    #balance = property(fget = get_balance, fset = set_balance, fdel = delete_balance)


a = BankAccount('Ivan', 1000)
print(a.my_balance)
a.my_balance = 1
del a.my_balance
