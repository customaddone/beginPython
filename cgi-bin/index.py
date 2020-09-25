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
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

# ABC004 マーブル
R, G, B = getNM()

dp = [[float('inf')] * (R + G + B + 1) for i in range(2001)]
dp[0][R + G + B] = 0

# 残り個数により置くボールの色が変化する
# ボールを置くコストも変化する
def judge(point, ball):
    if ball > G + B:
        return abs(point - (-100))
    elif G + B >= ball > B:
        return abs(point)
    else:
        return abs(100 - point)

for i in range(1, 2001):
    for j in range(R + G + B, -1, -1):
        if j == R + G + B:
            dp[i][j] = dp[i - 1][j]
        else:
            # i - 1000の地点にj + 1ボールを置き,残りはj個
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1] + judge(i - 1000, j + 1))
print(dp[2000][0])

# ABC017 D - サプリメント
N, M = getNM()
F = getArray(N)

# 何通り　→ comb or dp
# O(N)で
# 同じ味のサプリメントを摂取しない
# dp[i]:i日目までにサプリを摂取する通りが何通りあるか
# dp[i]:サプリi個目までにサプリを摂取する通りが何通りあるか

# N, M = 5, 2
# L = [1, 2, 1, 2, 2]の場合
# dp[0] = 1
# dp[1] = 1 1個目を新たに食べた場合、それ以前の通りは1通り
# dp[2] = 2 2個目を新たに食べた場合、それ以前の通りは2通り
# (前回1個目を食べたかもしれないし、今回1個目と合わせて2個目を食べたかもしれない)
# dp[i] += dp[（最後にF[i]が登場した場所）] ~ dp[i - 1]

dp = [0] * (N + 1) # dpだけ1-index
dp[0] = 1
ignore = [0] * (M + 1)
l = 0
now = dp[0]
for r in range(N):
    # 最初ignoreのフラグが立っていないが,nowにはdp[0]の値が入っている状態
    while ignore[F[r]]:
        ignore[F[l]] = 0 # F[l]のフラグを消す
        now -= dp[l] # lの直前のdpを引く
        now %= mod
        l += 1
    # dpをレコード（範囲の合計を足す）
    dp[r + 1] = now
    # rを1個ずらして更新
    now += dp[r + 1]
    now %= mod
    ignore[F[r]] = 1

print(dp)

# ABC044 C - 高橋君とカード
# 平均はQ[i] -= Aしとく
N, A = getNM()
Q = getList()
for i in range(N):
    Q[i] -= A

dp = [[0] * 5002 for i in range(N + 1)]
dp[0][2501] = 1

for i in range(1, N + 1):
    for j in range(5002):
        dp[i][j] += dp[i - 1][j]
        if 0 <= j - Q[i - 1] <= 5001:
            dp[i][j] += dp[i - 1][j - Q[i - 1]]

print(dp[-1][2501] - 1)

# ABC071 D - Coloring Dominoes
N = getN()
S1 = input()
S2 = input()
dp = [0 for i in range(N)]
if S1[0] == S2[0]:
    dp[0] = 3
else:
    dp[0] = 6
# i - 1個目、i個目が
# 横ドミノ１個目→横ドミノ２個目
# 横ドミノ→横ドミノ
# 横ドミノ→縦ドミノ
# 縦ドミノ→縦ドミノ
# 縦ドミノ→横ドミノそれぞれについて場合分け
# 各回について
for i in range(1, N):
    # 横ドミノ２つ目だった場合
    if S1[i] == S1[i - 1]:
        dp[i] = dp[i - 1]
    # 横ドミノ１つめor縦ドミノ１つ目の場合
    else:
        # 縦ドミノ１つ目
        if S1[i] == S2[i]:
            # 一つ前も縦ドミノ
            if S1[i - 1] == S2[i - 1]:
                dp[i] = (dp[i - 1] * 2) % mod
            # 横ドミノ
            else:
                dp[i] = dp[i - 1]
        # 横ドミノ1つ目
        else:
            # 一つ前が縦ドミノ
            if S1[i - 1] == S2[i - 1]:
                dp[i] = (dp[i - 1] * 2) % mod
            # 一つ前が２つ目横ドミノ
            else:
                dp[i] = (dp[i - 1] * 3) % mod
print(dp[-1])

# ABC074 C - Sugar Water
# ABが水、CDが砂糖、Eがとけられる量、Fが上限
A, B, C, D, E, F = getNM()

# A,Bを好きな回数使うことでi(0 <= i <= 30)の水を作り出せる
dp1 = [0] * 31
dp1[0] = 1
for i in range(1, 31):
    if i >= A:
        dp1[i] = max(dp1[i], dp1[i - A])
    if i >= B:
        dp1[i] = max(dp1[i], dp1[i - B])
waterlist = []
for i in range(31):
    if dp1[i] > 0:
        waterlist.append(i)

# C,Dを好きな回数使うことでi(0 <= i <= 3000)の砂糖を作り出せる
dp2 = [0] * 3001
dp2[0] = 1
for i in range(1, 3001):
    if i >= C:
        dp2[i] = max(dp2[i], dp2[i - C])
    if i >= D:
        dp2[i] = max(dp2[i], dp2[i - D])
sugerlist = []
for i in range(3001):
    if dp2[i] > 0:
        sugerlist.append(i)

ans = [0, 0]
concent = 0

for water in waterlist[1:]:
    if 100 * water <= F:
        left = F - (water * 100)
        # Fから水をひいた分、溶ける砂糖の限界を超えない量の砂糖を取得する
        index = bisect_right(sugerlist, min(left, E * water))
        suger = sugerlist[index - 1]
        # 濃度計算
        optconc = (100 * suger) / (100 * water + suger)
        # ここ>にすると濃度0%に対応できずWAに
        if optconc >= concent:
            concent = optconc
            ans = [100 * water + suger, suger]
print(*ans)
