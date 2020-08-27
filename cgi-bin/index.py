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

# N:ブロックの個数 M;ブロックの色 Y:コンボボーナス Z:全色ボーナス
# N <= 5000, M <= 10
N, M, Y, Z = getNM()
# 色ボーナス
d = dict()
for i in range(M):
    c, p = input().split()
    d[c] = (i, int(p))
# 落ちてくるブロックの種類
B = input()

# 全通り出してみよう
# 2 ** N通り
# 単色でやってみる?
# どれを取ればいいか
# 前から順に＾
# どの色をコンボしても点数は同じ

# dp?

# dp[i][j]: 直前の色がi, 全部でjの色を使った
dp = [[-float('inf')] * (1 << M) for _ in range(M + 1)]
dp[M][0] = 0

# 交換するdpの要領
for e in B:
    # B[i]番目の色ポイント
    i, p = d[e]
    # 色iを含む状態について調べる
    # 色が少ないものから順に巻き込んでいく感じ
    for j in range((1 << M) - 1, -1, -1):
        if j & (1 << i) == 0:
            continue

        # 候補1: 直前の色が違うものだった and 以前に使った色を使った
        num1 = max(dp[k][j] for k in range(M + 1) if k != i) + p
        # 候補2: 直前の色が同じものだった
        num2 = dp[i][j] + p + Y
        # 候補3: 直前の色が違うものだった and 以前に使っってない色を使った
        num3 = max(dp[k][j ^ (1 << i)] for k in range(M + 1) if k != i) + p
        dp[i][j] = max(dp[i][j], num1, num2, num3)

# 全色ボーナス
for i in range(M):
    dp[i][(1 << M) - 1] += Z

ans = 0
for row in dp:
    ans = max(ans, max(row))
print(ans)
