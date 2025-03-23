# EXPECTED INPUT:
# 3
# 3 7
# 15 7
# 5 2
# EXPECTED OUTPUT:
# 260

n = int(input())

confetti_list = []
for _ in range(n):
    row = map(int, input().strip().split(" "))
    confetti_list.append(list(row))

result = 0
for row in range(1, 101):
    for col in range(1, 101):
        for confetti in confetti_list:
            if (confetti[0] <= row < confetti[0] + 10) and (
                confetti[1] <= col < confetti[1] + 10
            ):
                result += 1
                break

print(result)
