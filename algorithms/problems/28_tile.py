# EXPECTED INPUT:
# 6 0
# 5 3 5 4 0 1
# 1 4 2 3 5 5
# 0 3 0 5 5 1
# 4 5 4 5 1 4
# 4 2 4 1 4 4
# 2 5 3 0 2 2
# EXPECTED OUTPUT:
# -1

N, K = map(int, input().split())
tile = [list(map(int, input().split())) for _ in range(N)]
INF = res = 10000
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
exit_dir = [
    [1, -1, -1, 2],  # 0
    [3, 2, -1, -1],  # 1
    [-1, -1, 1, 0],  # 2
    [-1, 0, 3, -1],  # 3
    [0, -1, 2, -1],  # 4
    [-1, 1, -1, 3],  # 5
]


# 경로 있으면 경로 길이 반환
# 경로 없으면 INF 반환
def get_dist():
    dist = 0
    r, c, d = 0, -1, 1
    while 1:
        r += dr[d]
        c += dc[d]
        if r == N - 1 and c == N:
            return dist
        if r < 0 or r >= N or c < 0 or c >= N:
            return INF
        d = exit_dir[tile[r][c]][d]
        if d == -1:
            return INF

        dist += 1

    return dist


if K == 0:
    res = get_dist()
else:
    for i in range(N):
        for j in range(N):
            org_num = tile[i][j]
            for new_num in range(6):
                if org_num == new_num:
                    continue
                tile[i][j] = new_num
                res = min(res, get_dist())
            tile[i][j] = org_num

print(res if res < INF else -1)
