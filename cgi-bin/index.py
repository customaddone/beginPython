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
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

''' ABC104 D - We Love ABC
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
'''

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
