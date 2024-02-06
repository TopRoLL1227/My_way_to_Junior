def decorator(practise):
    def multiplay(*args, **kwargs):
        print(f'Result is: {args}, {kwargs}')
        res = practise(*args, **kwargs)
        print(f'There is {practise.__name__}')
        return res
    return multiplay
    

@decorator
def mathematic(a, b):
    return a * b

@decorator
def school(a, b):
    return a + b

print(school(5, 5))
print(mathematic(2, 5))