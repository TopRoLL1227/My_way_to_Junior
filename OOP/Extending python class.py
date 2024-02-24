# Розширення класу - це створення атрибуту чи метода, якого немає в батьківському класі

class Person:
    
    def breathe(self):
        print('People breath')


class Doctor(Person):

    def sleep(self):
        print("Doctor sleep")

p = Person()
#p.sleep()

d = Doctor()
p.breathe()
d.breathe() 
  