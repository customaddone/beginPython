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

N, M = getNM()
F = getArray(N)

dp = [0] * (N + 1)
dp[0] = 1
ignore = [0] * (M + 1)
r, l = 0, 0
now = dp[0]
for r in range(N):
    # 左をずらす
    # iまで食べる日の前日までにjまで食べた場合、その通りがdp[j]通りある
    # なので影響する範囲は１日で食べられるところまで
    while ignore[F[r]]:
        ignore[F[l]] = 0
        now -= dp[l]
        now %= mod
        l += 1
    dp[r + 1] = now
    now += dp[r + 1]
    now %= mod
    ignore[F[r]] = 1
    r += 1
print(dp[N])
