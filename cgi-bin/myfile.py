def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

"""
N <= 1000
ブロックの価値の総和の最大値
N個のブロックのうちいくつか選んで任意の順序で
上に乗るブロックはブロックiのs以下でないといけない

どのブロックを選ぶか、どの順番で並べるか　dpしたくなる
小さいブロックから作っていく

総重量がwの時の最大値
4
1 2 10
3 1 10
2 4 10
1 6 10

[[1, 2, 10], [1, 6, 10], [2, 4, 10], [3, 1, 10]] の時
耐重量でソート
[[3, 1, 10], [1, 2, 10], [2, 4, 10], [1, 6, 10]]
どのようにしたらトポロジカルに

[[3, 1, 10], [1, 2, 10], [2, 4, 10], [1, 6, 10]]
[0, 0, 0, 10, 10, 0, 0, 0, 0, 0]
[0, 10, 10, 10, 10, 0, 0, 0, 0, 0]
[0, 10, 10, 20, 20, 20, 20, 0, 0, 0]
[0, 10, 20, 20, 30, 30, 30, 30, 0, 0]
ソートするのは間違い
ブロックを何個か選んで適当に並び替えたらそれは条件を満たせるか
下のsの方が小さいとは限らない
一つ目に何を置くか　順番が重要

小さい順からつんていく　積むとそのブロックのsはもう必要なくなる
[[], [[3, 10]], [[1, 10]], [], [[2, 10]], [], [[1, 10]], [], [], []]
[3, 10]が使われない？
融合させていくか
"""

for i in range(N + 1):
    for j in range(32):
        if A[i] & (1 << j):
            bit[j].add(i, 1)
            print(i, j)
            print(bit[j].cum(i, i + 1))

for i in range(N + 1):
    cnt = 0
    for j in range(32):
        # print(i, bit[j].get(i), j)
        cnt += (bit[j].cum(i, i + 1) % 2) * (2 ** j)
    print(cnt)



for t, x, y in T:
    if t == 1:
        for i in range(32):
            if y & (1 << i):
                bit[i].add(x, 1)
    else:
        cnt = 0
        for i in range(32):
            cnt += (bit[i].cum(x, y + 1) % 2) * (2 ** i)
