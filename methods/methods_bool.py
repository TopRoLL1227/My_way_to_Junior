# bit_length():
# Повертає кількість бітів, необхідних для представлення цього числа в двійковій системі числення (більше корисно для цілих чисел).
my_bool = True
bit_length = my_bool.bit_length()  # Для True поверне 1

# bool():
# Повертає True або False при виклику вбудованого булевого конструктора.
my_bool = True
bool_value = my_bool.__bool__()  # True

# eq(), ne():
# Порівнює два булевих значення на рівність (==) або нерівність (!=).
bool1 = True
bool2 = False
are_equal = bool1.__eq__(bool2)  # False
are_not_equal = bool1.__ne__(bool2)  # True
