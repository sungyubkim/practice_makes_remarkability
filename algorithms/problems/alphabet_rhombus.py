# EXPECTED INPUT:
# 4
# EXPECTED OUTPUT:
#       A
#     B M L
#   C N U T K
# D O V Y X S J
#   E P W R I
#     F Q H
#       G

n = int(input())
N = 2 * n - 1
A = [[" "] * N for _ in range(N)]
r, c, m, num = 0, n - 1, n - 1, 0

while 1:
    for dr, dc in zip([1, 1, -1, -1], [-1, 1, 1, -1]):
        for i in range(m):
            A[r][c] = chr(num + 65)
            num = (num + 1) % 26
            r += dr
            c += dc
    r += 1
    m -= 1
    if m == 0:
        A[r][c] = chr(num + 65)
        break

for a in A:
    print(*a)
