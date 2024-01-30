#  all() використовується для перевірки того, чи всі елементи в заданому ітерабельному об'єкті (такому як список, кортеж, множина і т.д.) є істинними. 

a = ['hello', 'hi', 'world']
print(all(a))  # True

a = ['hello', '', 'world']
print(all(a))  # False
####################################################
a = ['hello', 'hi', 'world']
print(any(a))  # True

a = ['hello', '', 'world']
print(any(a))  # True

a = ['', '', '']
print(any(a))  # False
####################################################

b = 100
condition_1 = b % 2 == 0
condition_2 = b > 5 
condition_3 = b < 1000

print(all([condition_1, condition_2, condition_3]))  # True
print(any((condition_1, condition_2, condition_3)))  # True