# EXPECTED INPUT:
# 32
# EXPECTED OUTPUT:
# 1 3 4
# 2 5 8
# 6 7 9

n = int(input())

result = [[-10 for i in range(n)] for i in range(n)]

cur_x = 0
cur_y = 0
direction = -1  # -1 is down-left // +1 is up-right


def move_pos(x, y, direction):
    if direction == 1:
        x -= 1
        y += 1
    else:
        x += 1
        y -= 1
    return x, y


for i in range(n**2):
    result[cur_x][cur_y] = i + 1
    # print("\n".join([" ".join(map(str, row)) for row in result]))
    if i == n**2 - 1:
        break

    # check next pos
    x, y = move_pos(cur_x, cur_y, direction)

    if x in [-1, len(result)]:
        direction *= -1
        if (cur_y + 1) <= len(result[cur_x]) - 1:
            cur_y += 1
        else:
            cur_x += 1
    elif y in [-1, len(result[x])]:
        direction *= -1
        if (cur_x + 1) <= len(result) - 1:
            cur_x += 1
        else:
            cur_y += 1
    else:
        cur_x, cur_y = x, y

print("\n".join([" ".join(map(str, row)) for row in result]))
