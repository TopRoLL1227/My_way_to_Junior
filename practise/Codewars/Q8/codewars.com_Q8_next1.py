#  Calculate BMI
def bmi(weight, height):
    if weight / height**2 <= 18.5:
        return "Underweight" 
    elif weight / height**2 <= 25.0:
        return "Normal"
    elif weight / height**2 <= 30:
        return 'Overweight'
    else:
        return 'Obese'
    
print(bmi(50, 1.80))

#  Beginner - Reduce but Grow
def grow(arr):
    c = 1
    for x in arr:
        c = c * x
        return c
    
print(grow([1, 2, 3, 4]))

#  Reversed sequence 
def reverse_seq(n):
    return [x for x in range(1, n + 1)[::-1]]

print(reverse_seq(5))

#  Count by X
def count_by(x, n):
    return[x * i for i in range(1, n + 1)]
    
#  If you can't sleep, just count sheep!!
def count_sheep(n):
    return ''.join(f'{x} sheep...' for x in range(1, n + 1))

#  def count_sheep(n):
#     sheep=""
#     for i in range(1, n+1):
#         sheep+=str(i) + " sheep..."
#     return sheep

#  Sum Mixed Array
def sum_mix(arr):
    return sum(int(x) for x in arr)

print(sum_mix([9, 3, '7', '3']))

#  The Feast of Many Beasts
def feast(beast, dish):
    return True if beast[0] == dish[0] and beast[:-2:-1] == dish[:-2:-1] else False

print(feast("great blue heron", "garlic naan"))

#  Transportation on vacation 
def rental_car_cost(d):
    return d * 40 if d < 3 else (d * 40) - 20 if d <= 4 <= 7 else (d * 40) - 50

print(rental_car_cost(4)) #230

#  Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    human = human_years
    cat = 0
    dog = 0
    for x in range(1, human_years + 1):
        if x == 1:
            cat += cat + 15
            dog += dog + 15
        elif x == 2:
            cat = cat + 9
            dog = dog + 9
        else:
            cat = cat + 4
            dog = dog + 5 
    return [human, cat, dog]

print(human_years_cat_years_dog_years(10))  # [10, 56, 64]

#  altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return ''.join([x.upper() if x == x.lower() else x.lower() for x in string])

print(to_alternating_case("ALTerNAtiNG CaSe"))