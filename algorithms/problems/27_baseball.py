# EXPECTED INPUT:
# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1
# EXPECTED OUTPUT:
# 2
from itertools import permutations

answer_list = list(permutations(list(range(1, 10)), 3))

num_shot = int(input().strip())

for i in range(num_shot):
    row = map(int, input().strip().split(" "))
    shot, strike, ball = list(row)
    shot = [int(s) for s in str(shot)]

    new_answer_list = []
    for answer in answer_list:
        _strike = 0
        for j in range(3):
            if shot[j] == answer[j]:
                _strike += 1
        if strike != _strike:
            continue

        _ball = len(set(shot).intersection(set(answer))) - strike
        if ball != _ball:
            continue

        new_answer_list.append(list(answer))

    answer_list = new_answer_list

    # print(shot, strike, ball, new_answer_list)


print(len(answer_list))
