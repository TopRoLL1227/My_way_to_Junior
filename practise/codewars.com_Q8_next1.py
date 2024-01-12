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


