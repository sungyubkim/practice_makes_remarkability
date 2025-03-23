# EXPECTED INPUT:
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
# 0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# EXPECTED OUTPUT:
# 1
# 3 2

board = []
for _ in range(19):
    row = map(int, input().strip().split(" "))
    board.append(list(row))


def check_win(board, r, c):
    turn = board[r][c]
    for dr, dc in zip([0, 1, -1, 1], [1, 0, 1, 1]):
        if (0 <= r - dr < 19) and (0 <= c - dc < 19):
            if board[r - dr][c - dc] == turn:
                continue
        i = 0
        can_win = True
        while can_win:
            i += 1
            if (
                not (0 <= r + dr * i < 19)
                or not (0 <= c + dc * i < 19)
                or board[r + dr * i][c + dc * i] != turn
            ):
                can_win = False
        if i == 5:
            return True
    return False


from itertools import product

for r, c in product(range(19), range(19)):
    if board[r][c] == 0:
        continue
    if is_win := check_win(board, r, c):
        print(board[r][c])
        print(f"{r+1} {c+1}")
        break
if not is_win:
    print(0)
