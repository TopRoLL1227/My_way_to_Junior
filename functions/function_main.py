# def name():
#     print(5)


# def func(par_1):
#     print(par_1)
#     print(name)

# func(1)

#print(func)


# CASE 1
# def func(par_1):
#     print(par_1)
# func()


# def add(a,b):
#     return a + b
# add(2)

# # CASE 2
# def func(par_1=2):
#     print(par_1)



# # CASE 3
# def func():
#     print("1")

# def func():
#     return 1,2

# def func1():


#     a , b = func()
#     print(a)
#     print(b)


# func1()

# def vova(x, y):
#     print(y, x)

# vova(y=10, x=20)


def num(*a):  # * Об'єднує аргументи в tuple
    print(a[2])  #  3
    return sum(a)  # 6

print(num(1, 2, 3))

def get_posts_info(**person):  # * Об'єднує аргументи в DICT
    print(person)  # {'name': 'Vova', 'posts_qty': 25}
    print(type(person))
    info = (
        f"{person['name']} wrote"
        f"{person['posts_qty']} posts"
    )
    return info

print(get_posts_info(name='Vova', posts_qty=25))


def get_posts_info(**person):
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info

print(get_posts_info(name='Vovik', posts_qty=25))  # Vovik wrote 25 posts

def get_posts_info(**person):
    print(person)
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info

print(get_posts_info(name='Vovik', posts_qty=25, id ='11'))

def update_car_info(**car):
    car['is_availabe'] = True
    return car

print(update_car_info(brand='Ducatti', price=1000))