# В Python docstring (document string) - це рядок документації, який розташований в початку модуля, класу, функції чи методу. 
# Його основна мета - надати короткий опис функції чи класу, щоб інші програмісти (і сам програміст через певний час) могли швидко зрозуміти, 
# як використовувати або розширювати даний код.

import random
import docstringModule

def get_even(lst):
    """Функція створює 
    список з парних чисел
    """
    even_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
    return even_lst
        
numbers = []
for x in range(10):
    numbers.append(random.randint(0, 9))

print('numbers:', numbers)
even = get_even(numbers)
print('even', even)

#help(get_even) # Функція створює список з парних чисел
#help(docstringModule)
help(docstringModule.Model)