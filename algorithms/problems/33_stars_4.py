# EXPECTED INPUT:
# 4
# EXPECTED OUTPUT:
# *
# **
# *​
# ***
# *
# **
# *
# ****
# *
# **
# *​
# ***
# *
# **
# *
# 26

n = int(input().strip())


def print_star(n, counter):
    if n == 1:
        counter += 1
        print("*")
        return counter
    else:
        counter = print_star(n - 1, counter)
        print("*" * n)
        counter += n
        counter = print_star(n - 1, counter)
        return counter


counter = print_star(n, 0)
print(counter)
