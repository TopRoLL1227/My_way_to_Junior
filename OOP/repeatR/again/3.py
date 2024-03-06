class Cat:

    breed = 'pers'


    def hello(*args):
        print("hello world from kitty", args)

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print("Nothing")

    def set_value(self, value, age = 10):
        self.name = value
        self.age = age
         

    


walt = Cat()
print(walt.__dict__)
walt.show_breed()
Cat.show_breed(walt)

walt.breed = 'siam'
walt.show_breed()
print(walt.__dict__)

mary = Cat()
mary.name = 'mary'
mary.show_name()


tom = Cat()
tom.set_value('Tom')
tom.show_name()

jerry = Cat()
jerry.set_value('jerry')
jerry.show_name()



# class Rep:

#     asd = 1

#     def num(self):
#         print(f'this is {self.asd}')


# a = Rep()
# a.num()
# a.asd = 2
# a.num()
