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

H, R = getNM()
G = [getList() for i in range(R)]

matrix = [[0] * R for _ in range(R)]
# staから1, 2...Rまで巡回する通り
def counter(sta):
    dp = [[0] * R for i in range(1 << R)]
    dp[1 << sta][i] = 1
    for bit in range(1, 1 << R):
        if not bit & (1 << sta):
            continue
        for s in range(R):
            if bit & (1 << s):
                for t in range(R):
                    if (bit & (1 << t)) == 0 and G[s][t]:
                        dp[bit|(1 << t)][t] = (dp[bit|(1 << t)][t] + dp[bit][s]) % mod

    for bit in range(2 ** R):
        for j in range(R):
            matrix[i][j] = (matrix[i][j] + dp[bit][j]) % mod

# 行列生成
for i in range(R):
    counter(i)

# matrixをH回[1, 0, 0...]にかける
logk = H.bit_length()
dp = [[[0] * R for i in range(R)] for i in range(logk)]
dp[0] = matrix

# 行列掛け算 O(n3)かかる
def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
            # 今回modをつける
            res[i][j] %= mod
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

# 行列の単位元
ans = [[0] * R]
ans[0][0] = 1

for i in range(logk):
    if H & (1 << i):
        ans = array_cnt(ans, dp[i])

print(ans[0][0] % mod)
