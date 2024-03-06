class Dog:

    breed = 'rottweiler'

    def set_value(self, name, age=0):
        self.name = name
        self.age = age

    def __init__(self):
        print('Hello new object is', self)


tommy = Dog()
tommy.set_value('tommy')
print(tommy.__dict__)