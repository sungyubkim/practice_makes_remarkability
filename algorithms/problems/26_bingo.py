# EXPECTED INPUT:
#  3 23  5  9 20
# 13  6 12 15 22
#  2  1 10 19 11
#  4 18 25 14 21
#  7 24 16  8 17
# 12 10 25 5 18
# 9 20 15 3 7
# 16 23 13 6 22
# 2 1 19 11 4
# 14 21 24 8 17
# EXPECTED OUTPUT:
# 12

board = []
for _ in range(5):
    row = list(filter(lambda x: len(x) > 0, input().strip().split()))
    row = list(map(int, row))
    board.append(list(row))

answer = []
for _ in range(5):
    row = map(int, filter(lambda x: len(x) > 0, input().strip().split(" ")))
    answer.extend(list(row))


def check_bingo(board):
    info_set = set()
    # horizontal check
    for row in range(len(board)):
        is_bingo = False
        for col in range(len(board[row])):
            if board[row][col] is not None:
                break
            if col == 4:
                is_bingo = True
        if is_bingo:
            info_set.add(f"h{row}")
    # vertical check
    for col in range(len(board[0])):
        is_bingo = False
        for row in range(len(board)):
            if board[row][col] is not None:
                break
            if row == 4:
                is_bingo = True
        if is_bingo:
            info_set.add(f"v{col}")
    # diagonal check
    for dr, dc in [[1, 1], [-1, 1]]:
        is_bingo = False
        if dr == 1:
            row, col = 0, 0
        else:
            row, col = 4, 0
        for _ in range(5):
            if board[row][col] is not None:
                break
            row += dr
            col += dc
            if _ == 4:
                is_bingo = True
        if is_bingo:
            info_set.add(f"d{dr}")
    return info_set


cnt_set = set()
for cnt, ans in enumerate(answer):
    # check ans as None
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ans:
                board[row][col] = None

    if cnt < 5:
        continue

    info_set = check_bingo(board)
    # for row in board:
    #     print(row)
    # print(info_set)
    if len(info_set) >= 3:
        break


print(cnt + 1)
