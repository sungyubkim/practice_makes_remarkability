# EXPECTED INPUT:
# 4
# 0
# 1 0
# 0 0 1
# 1 1 0 0
# 0
# 0 1
# 0 0 0
# 0 1 1 1
# EXPECTED OUTPUT:
# 2

N = int(input().strip())

A = []
for _ in range(N):
    row = map(int, input().strip().split(" "))
    A.append(list(row))

B = []
for _ in range(N):
    row = map(int, input().strip().split(" "))
    B.append(list(row))


def rotate(triangle):
    rotated = [[None for _ in range(len(row))] for row in triangle]
    new_c = N - 1
    for r in range(N):
        new_r = N - 1 - r
        for c in range(len(triangle[r])):
            rotated[new_r][new_c] = triangle[r][c]
            new_r = new_r + 1
        new_c = new_c - 1
    return rotated


def flip(triangle):
    flipped = [[None for _ in range(len(row))] for row in triangle]
    for r in range(N):
        new_c = len(triangle[r]) - 1
        for c in range(len(triangle[r])):
            flipped[r][new_c] = triangle[r][c]
            new_c = new_c - 1
    return flipped


def compute_dist(triangle, triangle_):
    result = 0
    for r in range(N):
        for c in range(len(triangle[r])):
            result += abs(triangle[r][c] - triangle_[r][c])
    return result


dist_arr = []
for _ in range(3):
    A = rotate(A)
    dist = compute_dist(A, B)
    dist_arr.append(dist)
    dist = compute_dist(flip(A), B)
    dist_arr.append(dist)

from functools import reduce

min_dist = reduce(min, dist_arr)
print(min_dist)
