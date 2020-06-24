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

N = 6
Q = [
[30, 35],
[35, 15],
[15, 5],
[5, 10],
[10, 20],
[20, 25]
]

dp = [[float('inf')] * N for i in range(N)]

def judge(a1, a2, a3):
    # [先頭][0] * [中間地点の一つ後][0] + [終点][1]
    return Q[a1][0] * Q[a2 + 1][0] * Q[a3][1]

def rec(r, c):
    minint = float('inf')
    for k in range(r, c):
        # 各中間地点kについてr, k, cを用いたdpであれやこれやする
        minint = min(minint, dp[r][k] + dp[k + 1][c] + judge(r, k, c))
    return minint

def matrix_chain(n):
    for i in range(n):
        dp[i][i] = 0

    for i in range(n):
        if i != n - 1:
            dp[i][i + 1] = dp[i][i] + dp[i + 1][i + 1] + judge(i, i, i + 1)

    for i in range(2, n):
        for j in range(0, n - i):
            # 例dp[0][3]についてrec(0, 3)
            dp[j][j + i] = rec(j, j + i)

    return dp

print(matrix_chain(N))
