mod = [0]
pw = 1
for c in input()[::-1]:
    # 大きい数字での計算方法
    # a と z が互いに素のとき
    # x == y (mod z)なら
    # ax == ay (mod z)
    # 10000 == 1924 (mod 2019)
    # 100000 == 19240 (mod 2019)
    # 100000 == 1060 (mod 2019) 前のpwに10で掛けた分を2019を割る
    mod.append((int(c) * pw + mod[-1]) % 2019)
    pw = pw * 10 % 2019
from collections import *
# 8646 % 2019 = 余り570
# 282668646 % 2019 = 余り570
# 282668646 - 8646 = 282660000
# 282660000 % 2019 = 140000 余り0
# 余りが同じものの個数をn(n - 1) / 2する
print(sum(v * (v - 1) // 2 for v in Counter(mod).values()))
