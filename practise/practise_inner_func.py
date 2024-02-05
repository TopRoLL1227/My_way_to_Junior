def my_func(func):
    def ny_func(*args):
        print("Hello, world")
        res = func(*args)
        print("Happy day!")
        return res
    return ny_func

def test(a):
    print('Yeap')
    return test

test = my_func(test)
test('a')