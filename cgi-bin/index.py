from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ABC178 E - Dist Max
# マンハッタン距離の最大値を答える
# ２点のマンハッタン距離はx - y同士、x + y同士のうちどちらか大きい方

N = getN()
que = [getList() for i in range(N)]

minus = []
plus = []
for x, y in que:
    minus.append(x - y)
    plus.append(x + y)
minus.sort()
plus.sort()
m = minus[-1] - minus[0]
p = plus[-1] - plus[0]
print(max(abs(m), abs(p)))

# ABC127 Cell distance
# マンハッタン距離はxとyとに分けて考えられる

"""
全ての通りは nmCk
平均値の考え方　
つまりO(N + M)の足し合わせみたいな
ダブった奴は割ったり引いたりすればいい

2 2 2なら
4 * 3 // 2! = 6通り　順列分あとでわる
nCr通りある
この中でマスiとjが同時に出現する確率は　一定のはず
iとjが同時に出現するのはn-2Ck-2通り
iとjの選び方 nC2通り
コストiになるペアがいくつあるか
iとjのコスト * n-2Ck-2 をnC2通りやる
nC2通りのうちいくつがコストi
H - a * W - b コストa + b
コストのとり方は最大でもN + M - 2数え上げ

マンハッタン距離は上下と左右別々に求められる

こういう問題でコストiを何回足したらいいかを考えるのは鉄則
コストの規則性が分かりづらい　分けて考える
コストiを何回足したらいいかは難しそう　マスiについてのコストの総和を求めればいい

(1, 1)について
横方向のマンハッタン距離
距離1: 1 * H個
距離2: 1 * H個...
距離W - 1: 1 * H個
つまり(1, 1)についてコストの合計はW(W - 1) // 2 * H * (n-2Ck-2)
これを(1, 1) ~ (H, 1)までH回やる

(1, 2)について
距離1: 1 * H個
距離2: 1 * H個...
距離W - 2: 1 * H個
(1, 2)についてコストの合計は(W - 1)(W - 2) // 2 * H * (n-2Ck-2)
これを(1, 2) ~ (H, 2)までH回やる

これを縦方向のマンハッタン距離でもやる

巨大数のcmbをどうやる？
n-2Ck-2
"""

lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

N, M, K = getNM()

ans = 0
for i in range(M - 1, 0, -1):
    ans += i * (i + 1) * (N ** 2) // 2
    ans %= mod

for i in range(N - 1, 0, -1):
    ans += i * (i + 1) * (M ** 2) // 2
    ans %= mod

print(ans * cmb(N * M - 2, K - 2) % mod)

#　Edu codeforces 111
# C. Manhattan Subarrays

# マンハッタン距離は45度回転
# マンハッタン距離がd(p, r) = d(p, q) + d(q, r)になってはいけない
# aのうち連続部分列を探せ

# 尺取り法な気がする 部分列は小さい方がいいので
# 新たに追加する要素を本当に含めても良いか
# 任意の２点を選ぶ？　TLE
# これをO(1)で判断できるように　いくつかのやばい点を通過できれば

# d(p, r) = d(p, q) + d(q, r)とは?
# (0, 1), (0, 2), (0, 3)ならout
# 点a, bが与えられる この２点が作る長方形内に入ってはいけない
# 点cが点a, bのなす長方形内に入ってない

# ２点が与えられるとO(1)で判断できる
# 点を増やすごとにこの条件は増えていく
# 最高4点までかも

T = getN()
for _ in range(T):
    N = getN()
    A = getList()

    def check(ar):
        if len(ar) < 3:
            return True
        n = len(ar)
        flag = True
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # i ~ k長方形内にjがあればout
                    if min(ar[i], ar[k]) <= ar[j] <= max(ar[i], ar[k]):
                        flag = False
        return flag

    l, ans = 0, 0
    for r in range(N):
        while not check(A[l:r + 1]):
            l += 1
        ans += (r - l + 1)
    print(ans)
