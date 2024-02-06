def validate_arguments(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:  # бо за допомогою виклику values() з'вляється допступ до всіх значень вибраного словаря
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be int or float!")
        result = fn(*args, **kwargs)
        return result
    

    return wrapper
    
@validate_arguments
def sum_numbs(a, b):
    return a + b


print(sum_numbs(7, 2))
print(sum_numbs(10.5, 2.3))
#print(sum_numbs(a = 10.5, b = '2.0'))

##########################################

def validate_arguments1(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:  # бо за допомогою виклику values() з'вляється допступ до всіх значень вибраного словаря
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be int or float!")
        result = fn(*args, **kwargs)
        return result
    

    return wrapper
    
@validate_arguments1
def sum_numbs1(a, b):
    return a + b

try:
    print(sum_numbs1(7, 2))
    print(sum_numbs1(10.5, 2.3))
    print(sum_numbs1(a = 10.5, b = '2.0'))
except ValueError as e:
    print(e)