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
