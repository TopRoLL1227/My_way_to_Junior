class Dog:

    breed = 'rottweiler'

    def hello(*args):
        print("Hello world from doggy", args)

    def show_breed(instance):  # сюди прилітає екземпляр класу
        print(f'my breed is {instance.breed}')
    

Dog.hello()

dooly = Dog()
print(Dog.hello)  # <function Dog.hello at 0x7f7149d86200>
print(dooly.hello)  # <bound method Dog.hello of <__main__.Dog object at 0x7f7149d56ef0>>


jack = Dog()
jack.hello()  # Hello world from doggy (<__main__.Dog object at 0x7fb78defaef0>,)
print(jack)   #                                                 0x7fb78defaef0>

dina = Dog()
dina.show_breed()  # my breed is rottweiler

#######################################################################################################
class Car:

    def bmw(self):
        print('g30 is a good auto')

    def audi(self, x, y):
        self.x = x
        self.y = y

    def get_audi(self):
        return self.x, self.y


Car.bmw(Car)

car = Car()
car.bmw()

new_car = Car()
new_car.audi(1, 2)
print(new_car.__dict__)

print(new_car.x)

print(new_car.y)

electro_car = Car()
electro_car.audi('E-tron', 'Fast')
print(electro_car.x)

print(electro_car.get_audi())

s = getattr(electro_car, 'get_audi')
print(s())