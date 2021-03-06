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

N, M = getNM()
query = [getList() for i in range(M)]
K = getN()
question = [getList() for i in range(K)]

dist = [[float('inf')] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0
for i in range(M):
    a, b, c = query[i]
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

# ワーシャルフロイド
def warshall_floyd(dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# まず一回回す
warshall_floyd(dist)

# 経路更新
# 距離の方を更新していけばO(K * N ** 2)で済む
for x, y, z in question:
    x -= 1
    y -= 1
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][x] + z + dist[y][j], dist[i][y] + z + dist[x][j])
    res = 0
    for i in range(N):
        for j in range(i + 1, N):
            res += dist[i][j]
    print(res)

# エッジ[u, v, c]が最短路を構成するか
# ワーシャル回したあとでやる

def needed_path(edges):
    m = len(edges)
    need_dist = [0] * m

    for i in range(N): # 全ての中間地点を試す
        for j in range(m):
            s, t, c = edges[j]
            s -= 1
            t -= 1
            # ぴったり最短路になるなら必要
            if dist[i][s] + c == dist[i][t]:
                need_dist[j] = 1

    return need_dist
