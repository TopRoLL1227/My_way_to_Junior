# Методи екземпляра

class Cat:
    
    def hello():
        print("Hello world kitty")

Cat.hello()
exem = Cat()  

print(Cat.hello)  # <function Cat.hello at 0x7fdba956e200>
print(exem.hello)  # <bound method Cat.hello of <__main__.Cat object at 0x7fdba953aef0>> 

print('##################################################################################################################')
#########################################################
class Cat1:
    
    def hello(*args):
        print("Hello world kitty", args)

asd = Cat1()
Cat1.hello()  # Hello world kitty
asd.hello()   # Hello world kitty (<__main__.Cat1 object at 0x7f0458156ef0>>,)
print(asd)    #                                             0x7f0458156ef0
zxc = Cat1()
zxc.hello()  # Hello world kitty (<__main__.Cat1 object at 0x7f706c357a00>,)
print(zxc)   #                                             0x7f706c357a00>

print('##################################################################################################################')
############################################################################

class Dog:
    
    breed = 'mops'
    
    def hello(*args):
        print("Hello world from puppy")

    def show_breed(instance):
        print(f'My breed is {instance.breed}')

    def show_name(instance):
        print(f'my name is {instance.name}')


walt = Dog()
print(walt.breed)
walt.show_breed()  # My breed is mops

walt.breed = 'rottweiler'
print(walt.breed)  # rottweiler
walt.show_breed()  # My breed is rottweiler

bob = Dog()
print(bob.breed)
bob.show_breed()

danny = Dog()
danny.name = 'Danny'
danny.show_name()
