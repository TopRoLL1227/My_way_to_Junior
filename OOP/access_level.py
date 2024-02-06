# Public attr

class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data_public(self):
        print(self.name, self.balance, self.passport)


account1 = BankAccount('Bob', 100000, 123456)  ####################
account1.print_data_public()  # Bob 100000 123456      #################### Ці два рядочки мають доступ до методу printdata


print(account1.name)           ############### 
print(account1.balance)        ############### Ці три рядочки мають доступ до методу __init__
print(account1.passport)       ###############



# Protected
# В Python атрибут, який має приступ "protected", позначається одним підкресленням перед ім'ям атрибуту (наприклад, _attribute).
# Атрибути з обмеженим доступом ("protected") вказують на те, що їх можна використовувати всередині класу і всередині підкласів, 
# але не слід прямо звертатися до них ззовні. Проте, в Python це лише конвенція, а не справжній механізм обмеження доступу, 
# тому можливо прямий доступ до таких атрибутів ззовні. Однак, програмісти зазвичай використовують такі атрибути з обмеженим доступом для того, 
# щоб натякнути іншим розробникам, що ці атрибути призначені для внутрішнього використання, і щоб зменшити ймовірність їхньої несправної зміни 
# або використання ззовні.

class BankAccount:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_data_protected(self):
        print(self._name, self._balance, self._passport)


account1 = BankAccount('Bob', 100000, 123456)  ####################
account1.print_data_protected()  # Bob 100000 123456      #################### Ці два рядочки мають доступ до методу printdata


print(account1._name)           ############### 
print(account1._balance)        ############### Ці три рядочки мають доступ до методу __init__
print(account1._passport)       ###############




# Private attr
# В Python атрибути з приватним доступом позначаються двома підкресленнями перед їхнім іменем (наприклад, __attribute).
# Атрибути з приватним доступом призначені для внутрішнього використання в межах класу, і їх не слід безпосередньо звертатися ззовні класу. 
# Це забезпечує більш високий рівень ізоляції для даних і методів класу, зменшуючи ризик непередбачених змін або використання ззовні.
# Проте, також варто зазначити, що в Python обмеження доступу до атрибутів це лише конвенція, а не справжній механізм. 
# Це означає, що доступ до приватних атрибутів все ще можливий ззовні класу, але вважається не рекомендованим і може ввести в оману інших розробників, які використовують клас.

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_data_private(self):
        print(self.__name, self.__balance, self.__passport)


account2 = BankAccount('Bob', 100000, 123456)  ####################
account2.print_data_private()  # Bob 100000 123456      #################### Ці два рядочки мають доступ до методу printdata


#print(account2.__name)           # AttributeError: 'BankAccount' object has no attribute '__name'
#print(account2.__balance)        # AttributeError: 'BankAccount' object has no attribute '__name'
#print(account2.__passport)       # AttributeError: 'BankAccount' object has no attribute '__name'

class Bank():

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def max_secret(self):
        self.__secret()


    def __secret(self):
        print(self.__name, self.__id)



top_secret = Bank('Jack', 30)
top_secret.max_secret()

# or

top_secret._Bank__secret()

#2

class Bank():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def secret(self):
        self.__topsecret()

    def __topsecret(self):
        print(self.name, self.id)

asd = Bank('Bob', 40)
asd.secret()

#or 

asd._Bank__topsecret()