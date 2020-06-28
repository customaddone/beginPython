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
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N, great_W = 4, 6
query = [
[2, 1],
[3, 4],
[4, 10],
[3, 4]
]
wei = []
val = []
for i in range(N):
    w, v = query[i]
    wei.append(w)
    val.append(v)

# 下限の数字て引く（あとで足し合わせた数 * wei_minを使う）
wei_min = min(wei)
for i in range(N):
    wei[i] -= wei_min

# ナップサック+部分和
def part_sum_5(n, k, limit, wei, val):
    dp = [[[0] * (limit + 1) for i in range(k + 1)] for i in range(n + 1)]

    # 足し合わせN個でvalができる
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(limit + 1):
                dp[i][j][l] = dp[i - 1][j][l]
                if l - wei[i - 1] >= 0:
                    dp[i][j][l] = max(dp[i - 1][j][l], dp[i - 1][j - 1][l - wei[i - 1]] + val[i - 1])

    res = 0
    for i in range(n + 1):
        for j in range(limit + 1):
            if i * wei_min <= (great_W - j):
                res = max(res, dp[N][i][j])

    return res

print(part_sum_5(N, N, 301, wei, val))
