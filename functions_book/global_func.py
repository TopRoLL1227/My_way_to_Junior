def my_fn():
    global a
    a = 10



my_fn()  # Обов'язково, після визову функції змінна global буде створена глобано
print(a)  # 10


b = 15

def my_new_fn():
    global b
    b = 25

my_new_fn()
print(b)  # 25

g = 50

def my_next_fn(a, b):
    print(g)
    print(a, b)

print(my_next_fn('xyz', 'abc'))  