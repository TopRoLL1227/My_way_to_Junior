my_string = "hello world"
capitalized_string = my_string.capitalize()  # "Hello world"

my_string = "hello world"
uppercased_string = my_string.upper()  # "HELLO WORLD"

my_string = "Hello World"
lowercased_string = my_string.lower()  # "hello world"

my_string = "hello world"
titled_string = my_string.title()  # "Hello World"

my_string = "Hello World"
swapped_string = my_string.swapcase()  # "hELLO wORLD" Може приймати аргумент chars

my_string = "hello world"
count = my_string.count('l')  # 3

my_string = "hello world"
index = my_string.find('l')  # 2

my_string = "hello world"
new_string = my_string.replace('world', 'Python')  # "hello Python"

my_string = "hello world"
starts_with_hello = my_string.startswith('hello')  # True

my_string = "hello world"
ends_with_world = my_string.endswith('world')  # True

my_string = "apple,orange,banana"
fruits_list = my_string.split(',')  # ['apple', 'orange', 'banana']

my_string = "   hello world   "
trimmed_string = my_string.strip()  # "hello world"

formatted_string = "Текст з {} i {}".format('змінна1', 'змінна2')  # "Текст з {} і {}".format(змінна1, змінна2)

words = ['Hello', ' ', 'World', '!']  # використовується для об'єднання (злиття) елементів ітерабельного об'єкта в один рядок. 
combined_string = ''.join(words)  # "Hello World!"

name = "Вася"
age = 25
message = "Мені {1} років, і мене звати {0}.".format(name, age)

print(message)





