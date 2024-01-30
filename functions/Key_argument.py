# 1) Вдубована функція
new_list = [3, 1, -4, 1, 5, -9, 2, -6, 5, 3, 5]
print(sorted(new_list, key = abs))  # [1, 1, 2, 3, 3, -4, 5, 5, 5, -6, -9]
# 2) Власна функція

def f(x):
    return x%10

new_list = [13, 19, 42, 1, 5, 95, 2, 61, 57, 3, 5]
print(sorted(new_list, key = f))  # [1, 61, 42, 2, 13, 3, 5, 95, 5, 57, 19]


a = [73, 10, 44, 55, 89, 74, 92]

def f(x):
    return x%2 == 1

print(sorted(a, key = f))

# 3) Вбудований метод об'єктів

a = ['bbb', 'CCC', 'WWW', 'qqq']

print(sorted(a, key = str.lower))
