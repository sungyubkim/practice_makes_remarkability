# EXPECTED INPUT:
# 4
# 3 7
# 5 2
# 15 7
# 13 14
# EXPECTED OUTPUT:
# 96

A = [[0] * 102 for _ in range(102)]

for _ in range(int(input())):
    sx, sy = map(int, input().split())
    for x in range(sx, sx + 10):
        A[x][sy : sy + 10] = [1] * 10

res = 0
for i in range(1, 101):
    for j in range(1, 101):
        if A[i][j]:
            for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                if A[i + dx][j + dy] == 0:
                    res += 1
print(res)
