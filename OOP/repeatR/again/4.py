class Cat:

    breed = 'pers'

    def set_value(self, value, age = 10):
        self.name = value
        self.age = age

    def __init__(self, name, breed = 'pers', age = 40, color = 'black'):
        print('hello', self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


#Cat('Tom', 'Siam', 40, 'black')

walt = Cat('Walt')
 