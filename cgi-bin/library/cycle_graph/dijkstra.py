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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# startからの距離を返す
# 計算量は(V + E)logV
# EがV ** 2(完全グラフ)に近づくと使えない

def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heapq.heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
    return dist

# 最短経路へのパス付きダイクストラ
def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]
    parent = [-1] * N

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        di, now = heappop(pq)
        if (di > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                parent[i[0]] = now
                heappush(pq, (dist[i[0]], i[0]))

    return dist, parent

# ARC008 THE☆たこ焼き祭り2012
# 完全グラフのダイクストラ
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
