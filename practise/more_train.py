def count_sheep(n):
    s = ''.join([f'{i} sheep...' for i in range(1, n + 1)])
    if isinstance(s, str):
        return s
    elif n == 0:
        return ''.join()


print(count_sheep(2)) #"1 sheep...2 sheep...3 sheep...")

