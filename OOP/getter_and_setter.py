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


    balance = property(fget = get_balance, fset = set_balance, fdel = delete_balance)



a = BankAccount('Ivan', 100000)
# print(a.name)
# a.balance = 'hello'

b = BankAccount('Vasya', 50000)
print(b.get_balance())
b.set_balance(20000)
print(b.get_balance())


print(b.__dict__)  # {'name': 'Vasya', '_BankAccount__balance': 20000}

c = BankAccount('Yarina', 9999)
print(c.get_balance())
c.set_balance(1000000)
print(c.get_balance())


d = BankAccount('Misha', 400)
print(d.balance)
d.balance = 444
print(d.balance)

del d.balance

# class Car:

#     def __init__(self, model, enginee):
#         self.__model = model
#         self.enginee = enginee

#     def get_model(self):
#         return self.__model
    
#     def set_model(self, m):
#         self.__model = m

    
#     cars = property(fget = get_model, fset = set_model)


# asd = Car('BMW', 3.0)
# print(asd.cars)
# asd.cars = 'Audi'
# print(asd.cars)

# print(asd.cars)
# asd.cars = 'MERCEDES'
# print(asd.cars)

# print(asd.cars)
# asd.cars = 'FERARI'
# print(asd.cars)