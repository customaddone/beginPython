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

# 集合[a1, a2...an]内で以下２つの条件を満たす部分集合の組(T, U)はいくつあるか問題
# 1: U ⊆ Tである
# 2: Uがある条件を満たす

# Tの中にUがいくつか含まれる
# ①iが進むごとにTの候補がn倍ずつ増えていく
# ②その後、Uを組むためのカウントを進める

ABC104 D - We Love ABC
S = '????C?????B??????A???????'
N = len(S)
# dp[i][j]: i番目にjまで丸をつけ終えている通り
dp = [[0] * 4 for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    # 通りの数を増やす
    for j in range(4):
        if S[i] != '?':
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
        else:
            dp[i + 1][j] += 3 * dp[i][j]
            dp[i + 1][j] %= mod

    # カウントが進むものを加える
    if S[i] == 'A' or S[i] == '?':
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][1] %= mod
    if S[i] == 'B' or S[i] == '?':
        dp[i + 1][2] += dp[i][1]
        dp[i + 1][2] %= mod
    if S[i] == 'C' or S[i] == '?':
        dp[i + 1][3] += dp[i][2]
        dp[i + 1][3] %= mod
print(dp[N][3] % mod)

# F - Knapsack for All Segments

"""
尺取りしそうで
要素分解する
成立したらあとは単純にかけていくやつ

成立したとこ: 左に伸ばす通り * 右に伸ばす通り
l = 0
total = 0
for r in range(N):
    total += A[r]
    while total > S:
        total -= A[l]
        l += 1
    if total == S:
        print(l, r)
N <= 3000?
連続部分和ではないのでナップサック
3 4
2 2 4
0:[1, 0, 0, 0, 0]
1: 足し合わせる[1, 0, 1, 0, 0]
 : 足し合わせない[1, 0, 1, 0, 0]
2: 足し合わせる[1, 0, 2, 0, 1]

前からi個までの要素で作った連続部分列の数N(N + 1)//2
f(none)[0]: 1
f(1, 1)[0]: 1 2を足さない
f(1, 1)[2]: 1 2を足す

2つめの2を考える
f(none)[0] + [2] = f(2, 2)
f(2, 2)[0]: 1 2を足さない
f(2, 2)[2]: 1 2を足す

f(1, 1)[0] + [2] = f(1, 2)
f(1, 2)[0]: 1 2を足さない
f(1, 2)[2]: 1 2を足す

f(1, 1)[2]: 1 2を足さない
f(1, 2)[4]: 1 2を足す

耳dpする
0: まだ領域に入っていない
1: 領域に入った
2: 領域から出た
"""

N, S = getNM()
A = getList()
MOD = 998244353

prev = [[0] * (S + 1) for j in range(3)]
prev[0][0] = 1

for a in A:
    next = [[0] * (S + 1) for j in range(3)]

    for j in range(S, -1, -1):
        # 足し合わせない場合
        next[0][j] += prev[0][j] # 1のみ
        next[0][j] %= MOD

        # 状態変化する
        next[1][j] += prev[0][j] + prev[1][j] # 既に侵入している通り + まだ侵入してない
        next[1][j] %= MOD

        # 足し合わせる場合
        if j - a >= 0:
            next[1][j] += prev[0][j - a] + prev[1][j - a]
            next[1][j] %= MOD

        # 状態変化する
        next[2][j] += prev[1][j] + prev[2][j]
        next[2][j] %= MOD

    prev = next

print((prev[1][-1] + prev[2][-1]) % MOD)


# ABC169 F - Knapsack for All Subsets
N, S = getNM()
A = getList()
MOD = 998244353

dp = [[0] * (S + 1) for i in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    # 通りの数を増やす
    for j in range(S + 1):
        dp[i + 1][j] += dp[i][j] * 2
        dp[i + 1][j] %= MOD
    # カウントが進むものを加える
    for j in range(S + 1):
        if j - A[i] >= 0:
            dp[i + 1][j] += dp[i][j - A[i]]
            dp[i + 1][j] %= MOD
print(dp[N][S] % MOD)
