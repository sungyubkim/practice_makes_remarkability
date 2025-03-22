# EXPECTED INPUT:
# 7
# EXPECTED OUTPUT:
# *
#  ***
#   *****
#    *******
#   *****
#  ***
# *

n = int(input())

result = ""

if not ((n <= 100) and (n % 2 == 1)):
    print("INPUT ERROR!")
else:
    for i in range(0, n // 2 + 1):
        result += " " * i + "*" * (2 * i + 1) + "\n"

    for i in reversed(range(0, n // 2)):
        result += " " * i + "*" * (2 * i + 1) + "\n"

    print(result)
