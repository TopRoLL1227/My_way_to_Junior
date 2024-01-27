def hello(a):
    return '0' if a % 2 == 0 else '1'

for i in range(1, 10 + 1):
    print(i, hello(i))




##############################################
    
def hello(a):
    print('0' if a % 2 == 0 else '1')

for i in range(1, 10 + 1):
    print(i, end=' ')
    hello(i)









