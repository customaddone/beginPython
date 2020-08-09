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

N, M = 2, 4
A, B = 2, 1
A -= 1
B -= 1
T = [3, 1]
D = [[1, 3, 3], [1, 4, 2], [2, 3, 3], [2, 4, 5]]
#d[i][j]:i→jへの距離
d = [[float("inf")] * M for i in range(M)]
for x, y, z in D:
   d[x - 1][y - 1] = z
   d[y - 1][x - 1] = z

# dp[i][j][l]: #訪れた集合がs、使ったチケットがj, 今いる点がvの時０に戻る最短経路
dp = [[[-1] * M for i in range(1 << N)] for i in range(1 << M)]

def rec(s, t, v, dp):
    if dp[s][t][v] >= 0:
        return dp[s][t][v]
     #全ての頂点を訪れた(s = 11...11 and v = 0)
    if v == B:
        dp[s][t][v] = 0
        return 0
    res = float('inf')
    for u in range(M):
        for j in range(N):
            # まだ未到達で、チケットが残っている場合
            if not s & (1 << u) and not t & (1 << j):
                # 道が無い場合はfloat('inf')
                # v → u1, u2...と探していく
                res = min(res, rec(s|(1 << u), t|(1 << j), u, dp) + d[v][u] / T[j])
    dp[s][t][v] = res
    return res
# 結局のところ0からスタートしようが1からスタートしようが同じ道を通る
print(rec(1 << A, 0, A, dp))
