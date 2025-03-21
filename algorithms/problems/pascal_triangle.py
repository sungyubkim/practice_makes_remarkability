# EXPECTED INPUT:
# 5 1
# EXPECTED OUTPUT:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

n, m = map(int, input().split(" "))

result = [[-10 for _ in range(i + 1)] for i in range(n)]


if not ((1 <= n <= 30) and (1 <= m <= 3)):
    print("INPUT ERROR!")
else:
    cur_x = 0
    cur_y = 0
    direction = 0

    for i in range(int(n * (n + 1) / 2)):
        # fill value
        if (i < 3) or (cur_y in [0, len(result[cur_x]) - 1]):
            val = 1
        else:
            val = result[cur_x - 1][cur_y - 1] + result[cur_x - 1][cur_y]
        result[cur_x][cur_y] = val

        # check pos
        if len(result[cur_x]) <= cur_y + 1:
            cur_x += 1
            cur_y = 0
        else:
            cur_y += 1

    if m == 1:
        print("\n".join([" ".join(map(str, row)) for row in result]))
    if m == 2:
        result_ = ""
        for i, row in enumerate(reversed(result)):
            result_ += " " * i + " ".join(map(str, row)) + " " * i + "\n"
        print(result_)
    if m == 3:
        result_transposed = [[-10 for _ in range(i + 1)] for i in range(n)]
        for i in range(len(result)):
            for j in range(len(result[i])):
                # use symmetry
                result_transposed[n - 1 - j][n - 1 - i] = result[i][j]
        print("\n".join([" ".join(map(str, row)) for row in result_transposed]))
