import itertools
l = ["a", "b", "c", "d"]

# 順番関係ありの組み合わせ
for v in itertools.permutations(l, 2):
    print(v)
# 関係なしの組み合わせ
for v in itertools.combinations(l, 2):
    print(v)
