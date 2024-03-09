class Person:
    
    def breath(self):
        print('Men breath')

    def sleep(self):
        print('Men sleep')

    def combo(self):
        self.breath()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()


class Doctor(Person):

    def breath(self):
        print('Doctor breath')

    def sleep(self):
        print('Doctor sleep')
 
    def walk(self):
        print('Doctor walk')


p = Person()
#p.combo()
d = Doctor()
d.combo()


