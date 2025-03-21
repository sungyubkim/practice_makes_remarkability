# EXPECTED INPUT:
# 5
# EXPECTED OUTPUT:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())

result = [[-10 for i in range(n)] for i in range(n)]


def move_pos(cur_x, cur_y, direction):
    if direction == 0:
        cur_y += 1
    if direction == 1:
        cur_x += 1
    if direction == 2:
        cur_y -= 1
    if direction == 3:
        cur_x -= 1
    return cur_x, cur_y


if not ((1 <= n <= 100)):
    print("INPUT ERROR!")
else:
    cur_x = 0
    cur_y = 0
    direction = 0
    for i in range(0, n**2):
        result[cur_x][cur_y] = i + 1

        if i < n**2 - 1:
            # check pos
            x, y = move_pos(cur_x, cur_y, direction)

            if result[x][y] > 0:
                direction = (direction + 1) % 4
                cur_x, cur_y = move_pos(cur_x, cur_y, direction)
            else:
                cur_x, cur_y = x, y
                if x in [0, n - 1] and y in [0, n - 1]:
                    direction = (direction + 1) % 4

        # print(i, cur_x, cur_y, direction)

    print("\n".join([" ".join(map(str, row)) for row in result]))
