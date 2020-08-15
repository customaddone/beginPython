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

N = 10
logk = N.bit_length()

# [Fi+2, Fi+1] = [[1, 1], [1, 0]][Fi+1, Fi]
# 一般項が出ない漸化式は行列の形に落とし込める
dp = [[[0, 0] for i in range(2)] for i in range(logk)]
dp[0] = [[1, 1], [1, 0]]

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
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

# 行列の単位元
ans = [[1, 0], [0, 1]]
for i in range(logk):
    if N & (1 << i):
        ans = array_cnt(ans, dp[i])

# [Fi+2, Fi+1] = [[1, 1], [1, 0]][Fi+1, Fi]より
# [Fn+1, Fn] = A ** n[F1, F0] = A ** n[1, 0]
# Fn = ans[1][0] * 1 + ans[1][1] * 0
print(array_cnt(ans, [[1], [0]])[1][0])
