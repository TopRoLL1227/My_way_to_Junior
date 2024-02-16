class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    



q = User('Ivan', 123)
print(q.password)
q.password = 'sss'
print(q.password)