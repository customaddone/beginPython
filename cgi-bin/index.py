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
from math import sqrt, pi
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

# N <= 2500のqueryに答える問題

# 面積kで焼くことができるたこ焼きの美味しさの最大値をf(k)とする時
# g(n) = max(f(1), f(2)... f(q))を求める問題

# f(n - 1) <= f(n)なので累積してg(n)を求めリストの形で持っておく

N = getN()
maze = [getList() for i in range(N)]
Q = getN()
query = getArray(Q)

# 二次元累積和
dp = [[0] * N for i in range(N)]
# 縦１行目、横１行目
for i in range(N):
    dp[i][0] = maze[i][0]
for i in range(N):
    for j in range(1, N):
        dp[i][j] = dp[i][j - 1] + maze[i][j]
# 全て
for i in range(1, N):
    for j in range(N):
        dp[i][j] += dp[i - 1][j]

# 採点マシーン
def judge(sx, sy, ex, ey):
    mother = dp[ey][ex]
    minus1 = 0
    minus2 = 0
    plus = 0
    if sx > 0:
        minus1 = dp[ey][sx - 1]
    if sy > 0:
        minus2 = dp[sy - 1][ex]
    if sx > 0 and sy > 0:
        plus = dp[sy - 1][sx - 1]
    return mother - minus1 - minus2 + plus

# 「大きさNの時の美味しさ」のリスト
anslist = [0] * (N ** 2 + 1)
for nsx in range(N):
    for nex in range(nsx, N):
        for nsy in range(N):
            for ney in range(nsy, N):
                opt = judge(nsx, nsy, nex, ney)
                #print(opt, [nsx, nsy, nex, ney])
                index = (nex - nsx + 1) * (ney - nsy + 1)
                anslist[index] = max(anslist[index], opt)

# 「大きさN以下の時の美味しさ」のリスト
ans_alta = [0] * (N ** 2 + 1)
for i in range(1, len(ans_alta)):
    ans_alta[i] = max(ans_alta[i - 1], anslist[i])

for i in query:
    print(ans_alta[i])
