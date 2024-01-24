def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)

rec(1)

