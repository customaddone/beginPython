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

N = 10
query = [
[7, 9],
[8, 1],
[9, 6],
[10, 8],
[8, 6],
[10, 3],
[5, 8],
[4, 8],
[2, 5]
]

dist = [[] for i in range(N)]
for i in range(N - 1):
    a, b = query[i]
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

dp = [[0, 0] for i in range(N)]
sta = 0
for i in range(N):
    if len(dist[i]) == 1:
        sta = i
        break

for i in range(N):
    if len(dist[i]) == 1 and i != sta:
        dp[i] = [1, 1]

ignore = [0] * N
ignore[sta] = 1
def dfs(now):
    white = 1
    black = 1
    for i in dist[now]:
        if ignore[i] != 1:
            ignore[i] = 1
            w_cnt, b_cnt = dfs(i)
            white = (white * (w_cnt + b_cnt)) % mod
            black = (black * w_cnt) % mod
    dp[now] = [white % mod, black % mod]
    return dp[now]

print(sum(dfs(sta)) % mod)
