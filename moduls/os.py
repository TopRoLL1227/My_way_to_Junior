import os

#  Модуль os в Python — це вбудований модуль, який надає доступ до функцій, специфічних для операційної системи, 
#  таких як робота з файловою системою, взаємодія з оточенням, виконання команд та інше.

# Основні функції та атрибути модуля os включають:

# Робота з каталогами та шляхами:

# os.getcwd(): Повертає поточний робочий каталог.
# os.chdir(path): Змінює поточний робочий каталог на заданий path.
# os.path.join(path1, path2, ...): Об'єднує шляхи відповідно до правил операційної системи.

# Робота з файлами та каталогами:
# os.listdir(path='.'): Повертає список файлів та папок у заданому каталозі.
# os.mkdir(path): Створює новий каталог за вказаним шляхом.
# os.remove(path): Видаляє файл за вказаним шляхом.
# os.rmdir(path): Видаляє пустий каталог за вказаним шляхом.

# Взаємодія з оточенням:
# os.environ: Словник, який містить змінні оточення.
# os.getenv(var_name, default=None): Повертає значення змінної оточення за іменем var_name або значення за замовчуванням, якщо така змінна не існує.

# Виконання команд:
# os.system(command): Виконує команду в оболонці.
# os.popen(command): Відкриває потік для взаємодії з виконаною командою.

import os

# Отримати поточний робочий каталог
current_directory = os.getcwd()
print("Поточний робочий каталог:", current_directory)

# Створити новий каталог
new_directory = os.path.join(current_directory, "новий_каталог")
os.mkdir(new_directory)
print("Створено новий каталог:", new_directory)

# Створити текстовий файл у новому каталозі
file_path = os.path.join(new_directory, "example.txt")
with open(file_path, "w") as file:
    file.write("Hello, world!")

# # Вивести список файлів та папок у поточному каталозі
# files_and_folders = os.listdir(current_directory)
# print("Список файлів та папок у поточному каталозі:", files_and_folders)

# # Вивести змінні оточення
# environment_variables = os.environ
# print("Змінні оточення:", environment_variables)

# # Викликати команду в оболонці
# os.system("echo 'Hello from the shell'")

# # Видалити створений файл
# os.remove(file_path)
# print("Видалено файл:", file_path)

# # Видалити створений каталог
# os.rmdir(new_directory)
# print("Видалено каталог:", new_directory)
