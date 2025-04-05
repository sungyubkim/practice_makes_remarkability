# EXPECTED INPUT:
# 96 61
# EXPECTED OUTPUT:
# 60

n, p = map(int, input().strip().split())

remainder_list = []

cur = n
while True:
    cur = (cur * n) % p
    if cur in remainder_list:
        idx = remainder_list.index(cur)
        break
    else:
        remainder_list.append(cur)

print(len(remainder_list) - idx)
