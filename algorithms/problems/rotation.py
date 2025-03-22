# EXPECTED INPUT:
# 5
# 3 4 1 2 3
# 2 3 4 5 6
# 2 3 4 6 7
# 1 7 6 5 4
# 6 8 9 3 4
# 90
# 0
# EXPECTED OUTPUT:
# 6 1 2 2 3
# 8 7 3 3 4
# 9 6 4 4 1
# 3 5 6 5 2
# 4 4 7 6 3

n = int(input())
square = []
for i in range(n):
    row = list(map(int, input().strip().split(" ")))
    square.append(row)

from copy import deepcopy

while True:
    angle = int(input())
    # exit cond.
    if angle == 0:
        break

    # check angle
    if not (angle in [90, 180, 270, 360]):
        continue

    # rotate
    rotated = deepcopy(square)

    if angle == 90:
        new_i, new_j = 0, n - 1
    elif angle == 180:
        new_i, new_j = n - 1, n - 1
    elif angle == 270:
        new_i, new_j = n - 1, 0
    elif angle == 360:
        new_i, new_j = 0, 0

    for i in range(n):
        for j in range(n):
            rotated[new_i][new_j] = square[i][j]

            if angle == 90:
                new_i = (new_i + 1) % n
            elif angle == 180:
                new_j = (new_j - 1) % n
            elif angle == 270:
                new_i = (new_i - 1) % n
            elif angle == 360:
                new_j = (new_j + 1) % n

        if angle == 90:
            new_j = (new_j - 1) % n
        elif angle == 180:
            new_i = (new_i - 1) % n
        elif angle == 270:
            new_j = (new_j + 1) % n
        elif angle == 360:
            new_i = (new_i + 1) % n

    square = rotated
    # print result
    for row in square:
        print(*row)
