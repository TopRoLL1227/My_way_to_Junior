def sum_array(arr):
    s = sum(sorted(arr)[1:-1])
    return s

print(sum_array([6, 2, 1, 8, 10]))


# s = [7, 3, 9, 1]
# print(sorted(s))