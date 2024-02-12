# # Алгоритм Евкліда

# a = int(input())
# b = int(input())

# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a

# print(a)



z = int(input())
x = int(input())

while z != x:
    if z > x:
        z = z - x
    else:
        x = x - z

print(z)