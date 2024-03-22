# Виключення бувають: 1) Виникають у момент запуску програми
#                     2) Виникають до запуску програми (Компіляції)

# SyntaxError: Виникає, коли в коді знаходиться синтаксична помилка, яка перешкоджає інтерпретатору Python правильно розуміти програмний код.
# IndentationError: Це виникає, коли виникають проблеми з відступами, наприклад, якщо вони не відповідають правилам форматування Python.
# NameError: Виникає, коли ім'я, яке використовується у програмі, не може бути знайдено. Наприклад, якщо спробувати використати змінну, яка не була оголошена.
# TypeError: Виникає, коли ви викликаєте функцію з аргументами неправильного типу або здійснюєте операції між об'єктами різних типів, які не підтримуються.
# ValueError: Виникає, коли функція отримує аргумент правильного типу, але неправильного значення.
# ZeroDivisionError: Виникає, коли спроба здійснити ділення на нуль.
# FileNotFoundError: Виникає, коли програма намагається відкрити файл, який не існує.
# KeyError: Виникає при спробі доступу до ключа в словнику, який не існує.
# IndexError: Виникає, коли ви намагаєтеся звернутися до елементу списку за індексом, який виходить за межі допустимих значень.
# Etc.


print('hello1')
print('hello2')
print('hello3')
#try:
#    print([1, 2][3])
#except LookupError:
#    print('list index pout of range')
try:
    int('789')
except ValueError:
    print('invalid literal')
print('hello4')
print('hello5')
print('hello6')


t = IndexError()
print(isinstance(t, IndexError))  # True
print(isinstance(t, LookupError))  # True
print(isinstance(t, TypeError))  # False