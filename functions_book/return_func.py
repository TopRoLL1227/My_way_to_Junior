def square(x):
    print(x ** 2)

a = square(6)  # 36 
print(a)  # None

#####################

def square(x):
    print(x ** 2)
    return x

a = square(6)  # 36 
print(a)  # None

######################

def blop(string):
    print(string + 'abc')
    return string

asd = blop('xzy')  # xzyabc
print(asd)  # xzy

######################

def wind(numb):
    return numb ** 2

print(wind(777))  # 603729

#####################
def fun():
    print(1)  # 1
    print(2)  # 2
    return 'hello'
    print(3)
    print(4)

print(fun())

#####################

def even(x):
    if x % 2 == 0:  # return x % 2 == 0
        return True
    else:
        return False
    

for i in range(2, 11 + 1, 2):
    print(i, even(i))