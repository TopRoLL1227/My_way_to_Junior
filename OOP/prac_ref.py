class Volodymyr():

    def add(self, a, b):
        self.a = a
        self.b = b

    def repeat(self):
        return self.a, self.b
    

alex = Volodymyr()
alex.add(100, 200)
print(alex.repeat())