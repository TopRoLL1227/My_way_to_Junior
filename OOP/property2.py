class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance
    
    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Balance need to be clear')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    my_balance = property()  # my_balance це властивість, а property це фукнція. Ця функція допомагає створювати властивості в класах.
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(get_balance)
    my_balance = my_balance.deleter(get_balance)
    #or
    #my_balance = property(get_balance)



a = BankAccount('Ivan', 100)
print(a.my_balance)  # get balance
                     # 100

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Навіщо звертатися до властивостей якщо можна викликати метод напряму?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Як звертатися до атрибутів класу виключно через властивості? За допомогою декоратора property.<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<