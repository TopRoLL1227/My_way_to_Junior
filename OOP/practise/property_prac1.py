class Car:

    def __init__(self, name, generation):
        self.__name = name
        self.__generation = generation

    def get_name(self):
        return self.__name
    
    def set_name(self, a):
        self.__name = a
        print(self.__name)
    
    def get_generation(self):
        return self.__generation
    
    def set_generation(self, a):
        self.__generation = a
        print(self.__generation)

    optional_name = property(get_name,set_name)
    optional_generation = property(get_generation, set_generation)


new_class = Car('BMW', 'f10')
print(new_class.optional_name)
new_class.optional_name = 'AUDI'
print(new_class.optional_name)

print(new_class.optional_generation)
new_class.optional_generation = 'f90'
print(new_class.optional_generation)