import itertools

# 4C3 * 3!
for i in itertools.permutations([0, 1, 2, 3], 3):
    print(i)

# 4C3
for i in itertools.combinations([0, 1, 2, 3], 3):
    print(i)
