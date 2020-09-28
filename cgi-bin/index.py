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
mod = 998244353

#############
# Main Code #
#############

# ABC036 D - 塗り絵
# 木dp
# 葉からボトムアップか頂点からdfs

N = getN()
query = [getList() for i in range(N - 1)]

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

# ABC133 E - Virus Tree 2
# 木dp
N, K = getNM()
query = [getList() for i in range(N - 1)]

dist = [[] for i in range(N)]
for a, b in query:
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

max_root = 0
max_root_index = 0
for i in range(N):
    if len(dist[i]) >= max_root:
        max_root = len(dist[i])
        max_root_index = i

pos = deque([max_root_index])

ans = 1
ignore = [-1] * N
ignore[max_root_index] = 1
ans *= cmb(K, max_root + 1) * math.factorial(max_root + 1)

while len(pos) > 0:
    u = pos.popleft()
    for i in dist[u]:
        if ignore[i] == -1:
            ignore[i] = 1
            if len(dist[i]) >= 2:
                ans *= cmb(K - 2, len(dist[i]) - 1) * math.factorial(len(dist[i]) - 1)
                ans %= mod
            pos.append(i)

print(ans % mod)
