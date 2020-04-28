# https://atcoder.jp/contests/arc054/tasks/arc054_b
# 求めるのは x + p * 2 ** (-2 * x / 3)の最小値
# == （上記の式）' == 0になるようなxを求める
# p * 2 ** (-2 * x / 3)の微分について
# u = -2 * x / 3とおくと
# dy/dx = dy/du * du/dx
# dy/du = p * 2 ** u log2 du/dx = -2 / 3より
# dy/dx = dy/du * du/dx = p * 2 ** u log2 * -2 / 3 = -2p / 3 log2 * 2 ** (-2 * x / 3)
# 1 - P * math.log(2) * (2/3) * 2 ** (-2x/3) となるxを求める
import math
p = float(input())
def f(x):
    # これを0にしたい（限りなく近づけたい)
    return 1 - (2 * p / 3) * math.log(2) * 2 ** (-2 * x / 3)

l = 0
r = p

# 0 ~ nの間の値で（候補がとても多い）ある条件を満たすものの最大値、最小値または極限値を求める
# 際に二分探索が使える
# 差が一定以下になるまで二分探索
# l < 0, r > 0のまま差がだんだんと縮まってくる
while r - l > 10 ** -10:
    mid = l + (r - l) /2
    # midがでかすぎるなら上限を下げる
    if f(mid) > 0:
        r = mid
    # midが小さすぎるなら下限を上げる
    else:
        l = mid

print(l + p / (2 ** (2 * l / 3)))
