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

# ARC008 THE☆たこ焼き祭り2012
# 完全グラフダイクストラ
N = 4
mem = [
[0, 0, 300, 10],
[0, 100, 10, 100],
[0, 200, 10, 200],
[0, 300, 10, 300]
]

dis = [float('inf')] * N
edges = []

def calc(x1, y1, x2, y2, speed):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance / speed

# 完全グラフのダイクストラだろうと0(NlogN)で求まる
def dijkstra(n, start):
    dist = [float('inf')] * n
    pos = [(0, start)]
    heapify(pos)
    dist[start] = 0

    while len(pos):
        cost, u = heappop(pos)

        if dist[u] < cost:
            continue
        # エッジは探索のたびに生成していく
        for i in range(N):
            if i == u:
                continue
            opt = calc(mem[i][0], mem[i][1], mem[u][0], mem[u][1], min(mem[u][2], mem[i][3]))
            if dist[u] + opt < dist[i]:
                dist[i] = dist[u] + opt
                heappush(pos, (dist[u] + opt, i))

    return dist

res = dijkstra(N, 0)
res.sort(reverse = True)

ans = 0
for i in range(N - 1):
    ans = max(ans, res[i] + i)

print(ans)

# ARC025 C - ウサギとカメ
# N:地点 M:道 R, T:ウサギ、カメの速さ
N, M, R, T = getNM()
edges = [[] for i in range(N)]
for i in range(M):
    a, b, c = getNM()
    edges[a - 1].append([b - 1, c])
    edges[b - 1].append([a - 1, c])

# ダイクストラである地点からの最小距離を求められるが
# NlogNダイクストラ
def dijkstra(n, start):
    dist = [float('inf')] * n
    pos = [(0, start)]
    heapify(pos)
    dist[start] = 0

    while len(pos):
        cost, u = heappop(pos)

        if dist[u] < cost:
            continue
        # エッジは探索のたびに生成していく
        for i, d in edges[u]:
            if dist[u] + d < dist[i]:
                dist[i] = dist[u] + d
                heappush(pos, (dist[u] + d, i))

    return dist

cnt = 0
for i in range(N):
    # iを目的地にした時の距離
    ar = sorted(dijkstra(N, i))[1:]
    # 小数使いたくない
    ar_t = [i * R for i in ar]
    ar_r = [i * T for i in ar]

    for i in range(N - 2, -1, -1):
        opt = bisect_left(ar_t, ar_r[i])
        # ウサギが亀より遅い場合のコーナーケース
        if opt > i:
            cnt += opt - 1
        else:
            cnt += opt
print(cnt)

# ABC099 C - Strange Bank
N = 44852

coin = [1]
sixsta = 6
while sixsta < 100000:
    coin.append(sixsta)
    sixsta *= 6

ninesta = 9
while ninesta < 100000:
    coin.append(ninesta)
    ninesta *= 9
coin.sort()

# NlogNダイクストラ
# これも最短経路を求める問題
def dijkstra(n, start):
    dist = [float('inf')] * n
    pos = [(0, start)]
    heapify(pos)
    dist[start] = 0

    while len(pos):
        cost, u = heappop(pos)

        if dist[u] < cost:
            continue
        # エッジは探索のたびに生成していく
        for i in range(len(coin)):
            if u + coin[i] >= n:
                continue
            if dist[u] + 1 < dist[u + coin[i]]:
                dist[u + coin[i]] = dist[u] + 1
                heappush(pos, (dist[u] + 1, u + coin[i]))

    return dist

print(dijkstra(N + 1, 0)[N])
