# def rec(x):
#     if len(x) == 1 or len(x) == 2:
#         return x
#     return x[0] + '(' + rec(x[1:-1]) + ')' + x[-1]
    
# x = input()
# print(rec(x))


s = 'malina'
print(s[0] + '(' + s[1:-1] + ')' + s[-1])  # m(alin)a