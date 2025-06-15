# EXPECTED INPUT:
# 1 2 3
# EXPECTED OUTPUT:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

t, n, k = map(int, input().strip().split())

from itertools import permutations

if t == 1:
    arr = [i for i in range(1, k + 1) for _ in range(n)]
else:
    arr = list(range(1, k + 1))

for pair in set(permutations(arr, n)):
    print(" ".join(map(str, pair)))
