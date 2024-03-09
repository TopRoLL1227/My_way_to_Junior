from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def password(self):
        print('getter called')
        return self.__password
    
    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False
    
    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError("Password must be string")
        if len(value) < 4:
            raise ValueError("Len must be more than 4 symbols")
        if len(value) > 12:
            raise ValueError("Len must be less than 12 symbols")
        if not User.is_include_number(value):
            raise ValueError("Password must have one or more numbers")

        self.__password = value


a = User('Bodya', 333)


a.password = 'asds1'
print(a.password)