#  Abbreviate a Two Word Name
def abbrev_name(name):
    g = [i[0]for i in name.split(' ')]
    s = '.'.join(g)
    j = s.upper()
    return(j)

print(abbrev_name('Devon Larrat'))

#  Convert number to reversed array of digits
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

print(digitize(23582357))

#  Returning Strings
def greet(name):
    return f'Hello, {name} how are you doing today?'

print(greet('John'))

#  A Needle in the Haystack
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))

#  Opposites Attract
def lovefunc(flower1, flower2):
    return True if flower1 % 2 == 0 and flower2 % 2 == 1 or flower1 % 2 == 1 and flower2 % 2 == 0 else False

print(lovefunc(1,4))

#  Beginner - Lost Without a Map
def maps(a):
    return [i*2 for i in a]

print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

#  Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0] == 'R' or name[0] == 'r' else f"{name} plays banjo"

print(are_you_playing_banjo('Rikki'))

#  Beginner Series #2 Clock
def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000

print(past(2,5,1))

#  Calculate average 
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

print(find_average([1, 2, 3]))

#  How good are you really?
def better_than_average(class_points, your_points):
    return True if your_points >= sum(class_points) / len(class_points) else False 

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))

#  Sum Arrays
def sum_array(a):
    s = 0
    if a == s:
        return 0
    else:
        return sum(a)

print(sum_array([1, 2, 3]))

#  Invert values
def invert(lst):
    return [-x for x in lst]

print(invert([-1,2,3,4,5]))

#  Simple multiplication
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9 

print(simple_multiplication(simple_multiplication(4)))

#  Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    positive_numbers = len([x for x in arr if x > 0])
    negative_numbers = sum([x for x in arr if x < 0])
    return [] if arr == [] else [positive_numbers, negative_numbers]

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))

#  Fake Binary
def fake_bin(x):
    return ''.join('0' if i < '5' else '1' for i in x)

print(fake_bin("45385593107843568"))

# str_numb = '45385593107843568'
# c = ''
# for x in str_numb:
#     if int(x) < 5:
#         c = c + '0'
#     else:
#         c = c + '1'
