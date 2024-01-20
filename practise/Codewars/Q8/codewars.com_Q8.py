
import math

#  Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(1))

#  Sum of positive
def positive_sum(arr):
    g = 0
    for x in arr:
        if x > 0:
            g = g + x
    return g

print(positive_sum([-1,2,3,4,-5])) 

#  Return negative
def make_negative(number):
    return -number if number > 0 else number

print(make_negative(1))

#  Reversed Strings
def solution(string):
    return string [::-1]

print(solution('world'))

#  Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return 'Yes' if boolean == True else 'No'

print(bool_to_word(True))

#  Opposite number
def opposite(number):
    if number > 0:
        return -number
    else:
        return -number
    
print(opposite(-3.1458))

#  Remove First and Last Character
def remove_char(s):
    return s[1:-1]

print(remove_char('asdfghj'))

#  Square(n) Sum
def square_sum(numbers):
    return sum(x**2 for x in numbers)

print(square_sum([1 ,2 ,2 ,4]))

#  Grasshopper - Summation
def summation(num):
    return sum(x for x in range(1, num+ 1))

print(summation(5))

#  Remove String Spaces
def no_space(x):
    return x.replace(' ', '')

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))

#  Basic Mathematical Operations
def basic_op(operator, value1, value2):
    g1 = value1 + value2
    g2 = value1 - value2
    g3 = value1 * value2
    g4 = value1 / value2
    if operator == '+':
        return g1
    elif operator == '-':
        return g2
    elif operator =='*':
        return g3
    else:
        return g4
    
print(basic_op('*', 5, 5))

#  Math
def litres(time):
    return math.floor(time / 2)  # time // 2

print(litres(12.3))

#  Century From Year
def century(year):
    return math.ceil(year / 100)

print(century(1701))