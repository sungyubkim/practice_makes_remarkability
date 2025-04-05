# EXPECTED INPUT:
# 4
# EXPECTED OUTPUT:
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1
# 24

n = int(input().strip())


def factorial(n):
    if n == 1:
        print("1! = 1")
        return 1
    else:
        print(f"{n}! = {n} * {n-1}!")
        res = factorial(n - 1)
        return n * res


res = factorial(n)
print(res)
