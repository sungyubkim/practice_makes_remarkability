# EXPECTED INPUT:
# 5 50
# EXPECTED OUTPUT:
# 7
# 12

d, k = map(int, input().strip().split(" "))

"""
1: a
2: b
3: a + b
4: a + 2b
5: 2a + 3b
6: 3a + 5b
7: 5a + 8b
fib(n-2) * a fib(n-1) * b
"""


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(d - 2), fib(d - 1))

b = 1
a = (k - fib(d - 1) * b) // fib(d - 2)
while (((k - fib(d - 1) * b)) % fib(d - 2)) != 0:
    b += 1
    a = (k - fib(d - 1) * b) // fib(d - 2)

print(a)
print(b)
