class Driver:

    def __init__(self, name):
        self.name = name


class Car:

    def __init__(self, model):
        self.model = model


class Heis(Driver, Car):

    def __init__(self, name, model):
        super().__init__(name)
        Car.__init__(self, model)

    def __str__(self):
        return f"{self.name}, {self.model}"

h = Heis('Shumaher', 'mercedes')
print(h)
        
d = Driver(h)
