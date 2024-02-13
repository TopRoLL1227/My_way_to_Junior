# def my_func():
#     for i in [1, 2, 3, 4]:
#         return i
    
# s = my_func()
# print(s)  # 1
# print(s)  #  1

def my_yield():
    for i in [1, 2, 3, 4]:
        yield i

g = my_yield()
#print(next(g))  # 1 
#print(next(g))  # 2
for x in g:
    print(x)