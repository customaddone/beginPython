#https://atcoder.jp/contests/abc145/tasks/abc145_c
from itertools import permutations
from math import factorial, hypot

n = int(input())
p = [list(map(int, input().split())) for i in range(n)]

ans = 0
# 全ての巡回方法についてpermutations
for ps in permutations(p, n):
    # １つ目の座標を取り出す
    x1, y1 = ps[0]
    for i in range(n):
        x2, y2 = ps[i]
        # hypot:math.sqrt((x1-x2)**2 + (y1-y2)**2)
        ans += hypot(x1-x2, y1-y2)
        # 座標を次のやつに
        x1, y1 = x2, y2
ans /= factorial(n)
print(ans)
