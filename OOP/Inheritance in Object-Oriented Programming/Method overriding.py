class Person:

    name = 'adam'

    def __init__(self, name):
        #print('init Person')
        self.name = name
    

    def breath(self):
        print('He is breathing')

    def walk(self):
        print('He is walking')

    def sleep(self):
        print('He is sleeping')

    def combo(self):
        self.breath()
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Person {self.name}'

class Doctor(Person):

    name = 'maria'

    def breath(self):
        print('He is not breathing')

    def __str__(self):
        return f'Doctor {self.name}'



d = Doctor('John')
p = Person('Adam' )
d.combo()


#print(p)  
#print(d)  