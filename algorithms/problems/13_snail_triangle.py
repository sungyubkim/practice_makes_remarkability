# EXPECTED INPUT:
# 6
# EXPECTED OUTPUT:
# 0
# 4 1
# 3 5 2
# 2 0 6 3
# 1 9 8 7 4
# 0 9 8 7 6 5

n = int(input())

result = [[-10 for _ in range(i + 1)] for i in range(n)]


def move_pos(cur_x, cur_y, direction):
    if direction == 0:
        cur_x += 1
        cur_y += 1
    if direction == 1:
        cur_y -= 1
    if direction == 2:
        cur_x -= 1
    return cur_x, cur_y


if not ((1 <= n <= 100)):
    print("INPUT ERROR!")
else:
    cur_x = 0
    cur_y = 0
    direction = 0

    for i in range(int(n * (n + 1) / 2)):
        result[cur_x][cur_y] = i % 10
        # print("\n".join([" ".join(map(str, row)) for row in result]))

        # check pos
        x, y = move_pos(cur_x, cur_y, direction)

        if (len(result) <= x) or (len(result[x]) <= y):
            # print(i, x, y, direction)
            direction = (direction + 1) % 3
            cur_x, cur_y = move_pos(cur_x, cur_y, direction)
            # print(i, cur_x, cur_y, direction)
            continue

        if result[x][y] >= 0:
            direction = (direction + 1) % 3
            cur_x, cur_y = move_pos(cur_x, cur_y, direction)
        else:
            cur_x, cur_y = x, y

    print("\n".join([" ".join(map(str, row)) for row in result]))
