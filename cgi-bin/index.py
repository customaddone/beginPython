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

lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod
    
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

# dfs

N, K = getNM()
dist = [[] for i in range(N)]
for i in range(N - 1):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

# 木dp的な
# 上から子ノードの塗り分け方、その子ノードの塗り分け方...をかけていく
def dfs(now, root): # 子ノードの塗り分け方は親がいればK-2Pr通り
    res = 1
    for i in dist[now]:
        if i != root:
            res *= dfs(i, now)
            res %= mod

    vari = (root != -1) + 1 # 親 + 自身 roots[u] == -1 なら親なし
    r = len(dist[now]) - (root != -1)
    res *= cmb(K - vari, r) * math.factorial(r)

    return res % mod

print((dfs(0, -1) * K) % mod)

# ABC146 D - Coloring Edges on Tree
N = getN()

dist = [[] for i in range(N)]
edges = {}
for i in range(N - 1):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)
    edges[(a - 1, b - 1)] = i
    edges[(b - 1, a - 1)] = i

color = [-1] * N
color[0] = 0
ans = [0] * (N - 1)
pos = deque([0])

while pos:
    u = pos.popleft()
    j = 1
    for i in dist[u]:
        if color[i] != -1:
            continue
        if j == color[u]:
            j += 1
        color[i] = j
        ans[edges[(i, u)]] = j
        pos.append(i)
        j += 1

print(max(ans))
for i in ans:
    print(i)
