from datetime import datetime

def average_numbers():
    summa = 0
    count = 0
    def inner(number):  # прийматиме число на вхід
        nonlocal summa
        nonlocal count
        summa = number + summa
        count = count + 1
        print(summa, count)  # 5 1
        return summa / count
    
    return inner

s = average_numbers()
print(s(5))  # 5.0
# print(s(10))
# print(s(25))

# s1 = average_numbers()
# print(s(10))
# print(s(20))
# print(s(30))


def timer():
    start = datetime.now()
    def time():
        return datetime.now() - start
    return time

s = timer()
print(s())