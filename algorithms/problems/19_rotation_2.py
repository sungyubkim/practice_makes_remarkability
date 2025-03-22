# EXPECTED INPUT:
# 6 2
# 123asd
# 456asd
# 0
# EXPECTED OUTPUT:
# 2 6
# 41
# 52
# 63
# aa
# ss
# dd

w, h = map(int, input().strip().split())

square = []
for _ in range(h):
    row = list(input().strip())
    square.append(row)

cmd = int(input())


def rotate_90(square):
    h, w = len(square), len(square[0])
    rotated = [[None for _ in range(h)] for _ in range(w)]  # (w, h)
    new_i, new_j = 0, h - 1
    for i in range(h):
        for j in range(w):
            rotated[new_i][new_j] = square[i][j]
            new_i = (new_i + 1) % w
        new_j = (new_j - 1) % h
    return rotated


def horizontal_flip(square):
    h, w = len(square), len(square[0])
    flipped = [[None for _ in range(w)] for _ in range(h)]  # (h, w)
    new_i, new_j = h - 1, 0
    for i in range(h):
        for j in range(w):
            flipped[new_i][new_j] = square[i][j]
            new_j = (new_j + 1) % w
        new_i = (new_i - 1) % h
    return flipped


def vertical_flip(square):
    h, w = len(square), len(square[0])
    flipped = [[None for _ in range(w)] for _ in range(h)]  # (h, w)
    new_i, new_j = 0, w - 1
    for i in range(h):
        for j in range(w):
            flipped[new_i][new_j] = square[i][j]
            new_j = (new_j - 1) % w
        new_i = (new_i + 1) % h
    return flipped


if 0 <= cmd <= 2:
    for i in range(cmd + 1):
        square = rotate_90(square)
elif cmd == 3:
    square = horizontal_flip(square)
elif cmd == 4:
    square = vertical_flip(square)

print(len(square[0]), len(square))
for row in square:
    print("".join(row))
