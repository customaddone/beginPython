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

M, P, X = input().split()
M = int(M)
X = int(X)
P = float(P)

# dp[i][j]: 残りラウンドiの時所持金jに到達できる確率
dp = [[0] * ((1 << M) + 1) for i in range(M + 1)]
dp[0][1 << M] = 1

for i in range(1, M + 1):
    for j in range((1 << M) + 1):
        # dp[i][j]にするものの中で最も確率が高いものを探す
        k = min(j, (1 << M) - j)
        ans = 0
        # 残りラウンドi - 1で所持金がj + l, j - lになるもので確率を求めてみる
        for l in range(k + 1):
            # P * dp[i - 1][j + l]: このラウンドで勝って次所持金j + lになる
            # (1 - P) * dp[i - 1][j - l]: このラウンドで負けて次所持金j - lになる
            # これら調べたもののうちの最大値
            ans = max(ans, P * dp[i - 1][j + l] + (1 - P) * dp[i - 1][j - l])
        # レコード
        dp[i][j] = ans

# 1000000 を 2 ** Mで区分けしたグループのうちどれに含まれるが
money_group = int(X / (1000000 / 2 ** M))
print(dp[M][money_group])


    #
