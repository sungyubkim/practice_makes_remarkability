# EXPECTED INPUT:
# 4 4 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# EXPECTED OUTPUT:
# 3 4 8 12
# 2 11 10 16
# 1 7 6 15
# 5 9 13 14

n, m, r = map(int, input().strip().split(" "))

square = []
for _ in range(n):
    row = map(int, input().strip().split(" "))
    square.append(list(row))

num_tornado = min(n, m) // 2

from copy import deepcopy


# single rotation
def rotate(square, r):
    rotated = deepcopy(square)
    for t in range(num_tornado):
        n_, m_ = n - 2 * t, m - 2 * t
        for _ in range(r % (2 * n_ + 2 * m_ - 4)):
            row, col = t, t
            d_row_list = (
                [1] * (n_ - 1) + [0] * (m_ - 1) + [-1] * (n_ - 1) + [0] * (m_ - 1)
            )
            d_col_list = (
                [0] * (n_ - 1) + [1] * (m_ - 1) + [0] * (n_ - 1) + [-1] * (m_ - 1)
            )
            val = rotated[row][col]
            for d_row, d_col in zip(d_row_list, d_col_list):
                new_row, new_col = row + d_row, col + d_col
                rotated[new_row][new_col], val = val, rotated[new_row][new_col]
                row, col = new_row, new_col
    return rotated


# rotate r times
square = rotate(square, r)

for row in square:
    print(*row)
