class Practise:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_pull(self):
        return self.__name
    
    def set_push(self, push):
        self.__old = push
        print(self.__old)

my_best = Practise('Vovik', 27)
print(my_best.get_pull())

my_best.set_push()

