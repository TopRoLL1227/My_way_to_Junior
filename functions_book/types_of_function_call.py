def f(a, b, c):
    print(a, b ,c)

# Позиційний
f(1, 5, 7)

# По найменуванні
f(b=10, c=20, a=5)

# Комбінований
f(2, c=10, b=20)

# По замовчуванню
def s(z, x, y='Unknown'):
    print(z, x, y)

s(1, 2)  # 1 2 Unknown
s(1, 2, 3)  # 1 2 3
