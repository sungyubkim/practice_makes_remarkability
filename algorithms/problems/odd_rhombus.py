# EXPECTED INPUT:
# 3
# EXPECTED OUTPUT:
# 6 1 8
# 7 5 3
# 2 9 4

n = int(input())

# init result
result = [[None for _ in range(n)] for _ in range(n)]

# fill values
cur_x, cur_y = 0, n // 2
for i in range(n**2):
    val = i + 1
    result[cur_x][cur_y] = val

    # move pos
    if val % n == 0:
        cur_x += 1
    else:
        cur_x = (cur_x - 1) % n
        cur_y = (cur_y - 1) % n

# print result
for row in result:
    print(*row)
